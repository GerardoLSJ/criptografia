   /* ESIME-CULHUACAN IPN, ALEJANDRO PADRON GODINEZ, 
 FUNDAMENTOS PARA LA CRIPTOGRAFIA, JUNIO DE 2008.
 Código para calcular el cifrado de flujo A5
 Esta es una versión que corre en Ubuntu 7.04 con gcc 4.1.4
*/

#include <stdio.h>


/* Máscaras para los registros de corrimiento*/
#define R1MASK  0x07FFFF /* 19 bits, enumerados del 0..18 */
#define R2MASK  0x3FFFFF /* 22 bits, enumerados del 0..21 */
#define R3MASK  0x7FFFFF /* 23 bits, enumerados del 0..22 */
#ifdef A5_1
#define R4MASK  0x01FFFF /* 17 bits, enumerados del 0..16 */
#endif /* A5_1 */


#ifndef A5_1
/* El bit de enmedio de los registros de corrimiento, para el reloj de control (bit apon A51)*/
#define R1MID   0x000100 /* bit 8 */
#define R2MID   0x000400 /* bit 10 */
#define R3MID   0x000400 /* bit 10 */
#else /* A5_1 */

/* Un bit de R4 que controla cada uno de los registros de corrimiento (registro clock unit), es la funcion de mayori para los registros*/
#define R4TAP1  0x000400 /* bit 10 */
#define R4TAP2  0x000008 /* bit 3*/
#define R4TAP3  0x000080 /* bit 7 */
#endif /* A5_1 */


/* Bits de Tapón o Retroalimentación, para el manejo de los registros.
 * Esto corresponde a los polinomios primitivos
 * x^19 + x^5 + x^2 + x + 1, x^22 + x + 1,
 * x^23 + x^15 + x^2 + x + 1, and x^17 + x^5 + 1. */

/*bit apon de R1, R2 R3 y R4*/
#define R1TAPS  0x072000 /* bits 18,17,16,13 */
#define R2TAPS  0x300000 /* bits 21,20 */
#define R3TAPS  0x700080 /* bits 22,21,20,7 */
#ifdef A5_1
#define R4TAPS  0x010800 /* bits 16,11 */
#endif /* A5_1 */


typedef unsigned char byte;
typedef unsigned long word;
typedef word bit;


/* Calcular la paridad de la palabra de 32-bit, i.e. la suma de sus bits modulo 2
*/
bit parity(word x) {
        x ^= x>>16;
        x ^= x>>8;
        x ^= x>>4;
        x ^= x>>2;
        x ^= x>>1;
        return x&1;
}


/* Reloj para el 1er registro. Para A5/1, cuando llega el Altimo bit del "frame" trama
 * is loaded in, one particular bit of each register is forced to '1';
 * that bit is passed in as the last argument. */

#ifndef A5_1
word clockone(word reg, word mask, word taps) {
#else /* A5_1 */
word clockone(word reg, word mask, word taps, word loaded_bit) {
#endif /* A5_1 */
        word t = reg & taps;
        reg = (reg << 1) & mask;
        reg |= parity(t);
#ifdef A5_2
        reg |= loaded_bit;
#endif /* A5_1 */
        return reg;
}


/* The three shift registers.  They're in global variables to make the code
 * easier to understand.
 * A better implementation would not use global variables. */
word R1, R2, R3;
#ifdef A5_2
word R4;
#endif /* A5_2 */


/* Return 1 iff at least two of the parameter words are non-zero. */
bit majority(word w1, word w2, word w3) {
        int sum = (w1 != 0) + (w2 != 0) + (w3 != 0);
        if (sum >= 2)      
                return 1;
        else
                return 0;
                 
}


/* Clock two or three of R1,R2,R3, with clock control
 * according to their middle bits.
 * Specifically, we clock Ri whenever Ri's middle bit
 * agrees with the majority value of the three middle bits.  For A5/2,
 * use particular bits of R4 instead of the middle bits.  Also, for A5/2,
 * always clock R4.
 * If allP == 1, clock all three of R1,R2,R3, ignoring their middle bits.
 * This is only used for key setup.  If loaded == 1, then this is the last
 * bit of the frame number, and if we're doing A5/2, we have to set a
 * particular bit in each of the four registers. */
void clock(int allP, int loaded) {
#ifndef A5_2
        bit maj = majority(R1&R1MID, R2&R2MID, R3&R3MID);
        if (allP || (((R1&R1MID)!=0) == maj))
                R1 = clockone(R1, R1MASK, R1TAPS);
        if (allP || (((R2&R2MID)!=0) == maj))
                R2 = clockone(R2, R2MASK, R2TAPS);
        if (allP || (((R3&R3MID)!=0) == maj))
                R3 = clockone(R3, R3MASK, R3TAPS);
                
        
    
                
       /* printf(" \n  R1TAPS:%08x",(unsigned int)R1TAPS); no marca nada
        printf(" \n  R2TAPS:%08x",(unsigned int)R2TAPS);
        printf(" \n  R3TAPS:%08x",(unsigned int)R3TAPS);*/
	
	/*printf("\n");		
		printf("%1d R1m:%08x",bit maj,(unsigned int)R1);
		printf("   R2m:%08x",(unsigned int)R2);
		printf("   R3m:%08x",(unsigned int)R3);*/

#else /* A5_2 */
        bit maj = majority(R4&R4TAP1, R4&R4TAP2, R4&R4TAP3);
        if (allP || (((R4&R4TAP1)!=0) == maj))
                R1 = clockone(R1, R1MASK, R1TAPS, loaded<<15);
        if (allP || (((R4&R4TAP2)!=0) == maj))
                R2 = clockone(R2, R2MASK, R2TAPS, loaded<<16);
        if (allP || (((R4&R4TAP3)!=0) == maj))
                R3 = clockone(R3, R3MASK, R3TAPS, loaded<<18);
        R4 = clockone(R4, R4MASK, R4TAPS, loaded<<10);
        
        
        
#endif /* A5_2 */
}


/* Generate an output bit from the current state.
 * You grab a bit from each register via the output generation taps;
 * then you XOR the resulting three bits.  For A5/2, in addition to
 * the top bit of each of R1,R2,R3, also XOR in a majority function
 * of three particular bits of the register (one of them complemented)
 * to make it non-linear.  Also, for A5/2, delay the output by one
 * clock cycle for some reason. */
bit getbit() {
        bit topbits = (((R1 >> 18) ^ (R2 >> 21) ^ (R3 >> 22)) & 0x01);
#ifndef A5_1
        return topbits;
#else /* A5_1 */
        static bit delaybit = 0;
        bit nowbit = delaybit;
        delaybit = (
            topbits
            ^ majority(R1&0x8000, (~R1)&0x4000, R1&0x1000)
            ^ majority((~R2)&0x10000, R2&0x2000, R2&0x200)
            ^ majority(R3&0x40000, R3&0x10000, (~R3)&0x2000)
            
           
            );
            
           
        return nowbit;
#endif /* A5_1 */
}


/* Do the A5 key setup.  This routine accepts a 64-bit key and
 * a 22-bit frame number. */
void keysetup(byte key[8], word frame) {
        int i;
        bit keybit, framebit;
	
	
        /* Zero out the shift registers. */
        R1 = R2 = R3 = 0;
#ifdef A5_1
        R4 = 0;
#endif /* A5_1 */


        /* Load the key into the shift registers,
         * LSB of first byte of key array first,
         * clocking each register once for every
         * key bit loaded.  (The usual clock
         * control rule is temporarily disabled.) */
        for (i=0; i<64; i++) {
                clock(1,0); /* always clock */
                keybit = (key[i/8] >> (int)(i&7)) & 1; /* The i-th bit of the key */
                R1 ^= keybit; R2 ^= keybit; R3 ^= keybit;
		
		printf("\n");		
		
		printf("%2d %02x %1d %02x %1d R1k:%08x",i,key[i/8],(int)i&7,(key[i/8] >> (i&7)),(int)keybit,(unsigned int)R1);
		printf("   R2k:%08x",(unsigned int)R2);
		printf("   R3k:%08x",(unsigned int)R3);
		

#ifdef A5_1
                R4 ^= keybit;
                

#endif /* A5_1 */
        }


        /* Load the frame number into the shift registers, LSB first,
         * clocking each register once for every key bit loaded.
         * (The usual clock control rule is still disabled.)
         * For A5/2, signal when the last bit is being clocked in. */
        for (i=0; i<22; i++) {
                clock(1,i==21); /* always clock */
                framebit = (frame >> i) & 1; /* The i-th bit of the frame # */
                R1 ^= framebit; R2 ^= framebit; R3 ^= framebit;
		
		printf("\n");	
		
		printf(" Frame %2d %1d R2f:%08x",i,(int)framebit, (unsigned int)R1);
		
		
		//printf("%2d %02x %1d %02x %1d R1f:%08x",i,frame[i/8],(int)i&7,(frame[i/8] >> (i&7)),(int)framebit,(unsigned int)R1);	
		//printf("   R1f:%08x",(unsigned int)R1);
		printf("   R2f:%08x",(unsigned int)R2);
		printf("   R3f:%08x",(unsigned int)R3);
		
#ifdef A5_2
                R4 ^= framebit;
               // printf("\n\n  el R4 tiene:%08x  \n",(unsigned int)R4);
#endif /* A5_1 */
        }


        /* Run the shift registers for 100 clocks
         * to mix the keying material and frame number
         * together with output generation disabled,
         * so that there is sufficient avalanche.
         * We re-enable the majority-based clock control
         * rule from now on. */
        for (i=0; i<100; i++) {
                clock(0,0);
        
        printf("\n");		
		printf(" MY %d  R1f:%08x",i,(unsigned int)R1);
		printf("   R2f:%08x",(unsigned int)R2);
		printf("   R3f:%08x",(unsigned int)R3);
		
		 
		    
        }
        
        /* For A5/1, we have to load the delayed output bit.  This does _not_
         * change the state of the registers.  For A5/1, this is a no-op. */
        getbit();
        
         
     // printf(" \n\nel getbit tiene:",getbit);
    // printf("\n\n  el getbit tiene:%08x  \n",(unsigned int)getbit);

	
	
        /* Now the key is properly set up. */
}


/* Generate output.  We generate 228 bits of
 * keystream output.  The first 114 bits is for
 * the A->B frame; the next 114 bits is for the
 * B->A frame.  You allocate a 15-byte buffer
 * for each direction, and this function fills
 * it in. */
void run(byte AtoBkeystream[], byte BtoAkeystream[]) {
        int i;


        /* Zero out the output buffers. */
        for (i=0; i<=113/8; i++)
                AtoBkeystream[i] = BtoAkeystream[i] = 0;
 

        /* Generate 114 bits of keystream for the
         * A->B direction.  Store it, MSB first. */
        for (i=0; i<114; i++) {
                clock(0,0);
                
               // AtoBkeystream[i];
                AtoBkeystream[i/8] |= getbit() << (7-(i&7));
               //printf ("\n\n  numeracion %d valor  AtoBkeystream:     %x  ",i,(unsigned char) AtoBkeystream[46] );
                
              //  printf("\n\n  %d salio: AtoBkeyStream tiene:%08x  \n",i,(unsigned int) AtoBkeystream[i] );  // muestra las salidas criptograficas
        }


        /* Generate 114 bits of keystream for the
         * B->A direction.  Store it, MSB first. */
        for (i=0; i<114; i++) {
                clock(0,0);
                
                BtoAkeystream[i] ;
                //BtoAkeystream[i/8] |= getbit() << (7-(i&7));
        	//	 printf ("\n\n  numeracion %d valor BtoAkeystream:     %x  ",i,(unsigned char) BtoAkeystream[40] );
		         // printf("\n\n %d salio: BtoAkeystream tiene:08%d \n",i,(unsigned int) BtoAkeystream[i] );  // muestra las salidas criptograficas
        }
}


/* Test the code by comparing it against
 * a known-good test vector. */
void test() {
#ifndef A5_1
        byte key[8] = {0x12, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF};
        word frame = 0x000134;
        byte goodAtoB[15] = { 0x53, 0x4E, 0xAA, 0x58, 0x2F, 0xE8, 0x15,
                              0x1A, 0xB6, 0xE1, 0x85, 0x5A, 0x72, 0x8C, 0x00 };
        byte goodBtoA[15] = { 0x24, 0xFD, 0x35, 0xA3, 0x5D, 0x5F, 0xB6,
                              0x52, 0x6D, 0x32, 0xF9, 0x06, 0xDF, 0x1A, 0xC0 };
#else /* A5_1 */
        byte key[8] = {0x00, 0xfc, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
        word frame = 0x21;
        byte goodAtoB[15] = { 0xf4, 0x51, 0x2c, 0xac, 0x13, 0x59, 0x37,
                              0x64, 0x46, 0x0b, 0x72, 0x2d, 0xad, 0xd5, 0x00 };
        byte goodBtoA[15] = { 0x48, 0x00, 0xd4, 0x32, 0x8e, 0x16, 0xa1,
                              0x4d, 0xcd, 0x7b, 0x97, 0x22, 0x26, 0x51, 0x00 };
#endif /* A5_1 */
        byte AtoB[15], BtoA[15];
        int i, failed=0;

        keysetup(key, frame);
        run(AtoB, BtoA);

        /* Compare against the test vector. */
        for (i=0; i<15; i++)
                if (AtoB[i] != goodAtoB[i])
                        failed = 1;
        for (i=0; i<15; i++)
                if (BtoA[i] != goodBtoA[i])
                        failed = 1;


        /* Print some debugging output. */
        printf("\n"); 
	printf("key: 0x");
        for (i=0; i<8; i++)
                printf("%02X", key[i]);
        printf("\n");
        printf("frame number: 0x%06X\n", (unsigned int)frame);
        printf("known good output:\n");
        printf(" A->B: 0x");
        for (i=0; i<15; i++)
                printf("%02X", goodAtoB[i]);
        printf("  B->A: 0x");
        for (i=0; i<15; i++)
                printf("%02X", goodBtoA[i]);
        printf("\n");/*
        printf("observed output:\n");
        printf(" A->B: 0x");
        for (i=0; i<15; i++)
                printf("%02X", AtoB[i]);
        printf("  B->A: 0x");
        for (i=0; i<15; i++)
                printf("%02X", BtoA[i]);
        printf("\n");*/


        if (!failed) {
                printf("Self-check succeeded: everything looks ok.\n");
                //exit(0);
        } else {
                /* Problems!  The test vectors didn't compare*/
                printf("\nI don't know why this broke; contact the authors.\n");
        }
}


int main(void) {
        test();
        return 0;
}

