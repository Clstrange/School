                .ORIG x3000
                BRnzp START
                PROMPT  .STRINGZ "Enter a command: "    
                ADDRESS .FILL PROMPT
                ADD_TEMP  .STRINGZ "0001"    
                ADD_OP .FILL ADD_TEMP
                AND_TEMP  .STRINGZ "0101"    
                AND_OP .FILL AND_TEMP
                TEMP  .STRINGZ "0000"    
                TEMP_OP .FILL TEMP
                JMP_TEMP  .STRINGZ "1100"    
                JMP_OP .FILL JMP_TEMP
                JSR_TEMP  .STRINGZ "0100"    
                JSR_OP .FILL JSR_TEMP
                JSRR_TEMP  .STRINGZ "0100"    
                JSRR_OP .FILL JSRR_TEMP
                LD_TEMP  .STRINGZ "0010"    
                LD_OP .FILL LD_TEMP
                LDI_TEMP  .STRINGZ "1010"    
                LDI_OP .FILL LDI_TEMP
                LDR_TEMP  .STRINGZ "0110"    
                LDR_OP .FILL LDR_TEMP
                LEA_TEMP  .STRINGZ "1110"    
                LEA_OP .FILL LEA_TEMP
                NOT_TEMP  .STRINGZ "1001"    
                NOT_OP .FILL NOT_TEMP
                RET_TEMP  .STRINGZ "1100"    
                RET_OP .FILL RET_TEMP
                RTI_TEMP  .STRINGZ "1000"    
                RTI_OP .FILL RTI_TEMP
                ST_TEMP  .STRINGZ "0011"    
                ST_OP .FILL ST_TEMP
                STI_TEMP  .STRINGZ "1011"    
                STI_OP .FILL STI_TEMP
                STR_TEMP  .STRINGZ "0111"    
                STR_OP .FILL STR_TEMP
                TRAP_TEMP  .STRINGZ "1111"    
                TRAP_OP .FILL TRAP_TEMP
                RESERVED_TEMP  .STRINGZ "1101"    
                RESERVED_OP .FILL RESERVED_TEMP 
                ; ASCII for the letters
                A       .FILL x0041
                B       .FILL x0042
                D       .FILL x0044
                E       .FILL x0045
                I       .FILL x0049
                J       .FILL x004A
                L       .FILL x004C
                M       .FILL x004D
                N       .FILL x004E
                O       .FILL x004F
                P       .FILL x0050
                Q       .FILL x0051
                R       .FILL x0052
                S       .FILL x0053
                T       .FILL x0054
                U       .FILL x0055
                V       .FILL x0056
                ENTER   .FILL x000A
                NEGATIVE .FILL #-32
                LOWER   .FILL x0014
                ; Prompt user
START           AND R0, R0, #0
                AND R1, R1, #0
                AND R2, R2, #0
                AND R3, R3, #0
                AND R4, R4, #0
                LD R4, NEGATIVE
                AND R5, R5, #0
                AND R6, R6, #0
                AND R7, R7, #0
                LD R0, ADDRESS
                PUTS
                ;Puts user input into R0
                GETC 

                ;Turning R2 to a negative number        
                LD R2, A
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'A'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_A

                ;Check for 'a'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_A

                ;Turning R2 to a negative number        
                LD R2, B
                NOT R2, R2
                ADD R2, R2, #1            

                ;Check for 'B'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_B

                ;Check for 'b'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_B

                ;Turning R2 to a negative number        
                LD R2, J
                NOT R2, R2
                ADD R2, R2, #1            

                ;Check for 'J'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_J

                ;Check for 'j'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_J

                ;Turning R2 to a negative number        
                LD R2, L
                NOT R2, R2
                ADD R2, R2, #1      

                ;Check for 'L'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_L

                ;Check for 'l'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_L

                ;Turning R2 to a negative number        
                LD R2, N
                NOT R2, R2
                ADD R2, R2, #1   

                ;Check for 'N'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_N

                ;Check for 'n'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_N

                ;Turning R2 to a negative number        
                LD R2, R
                NOT R2, R2
                ADD R2, R2, #1 

                ;Check for 'R'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_R

                ;Check for 'r'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_R

                ;Turning R2 to a negative number        
                LD R2, S
                NOT R2, R2
                ADD R2, R2, #1 

                ;Check for 'S'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_S

                ;Check for 's'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_S

                ;Turning R2 to a negative number        
                LD R2, T
                NOT R2, R2
                ADD R2, R2, #1 

                ;Check for 'T'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_T

                ;Check for 't'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_T

                ;Turning R2 to a negative number        
                LD R2, Q
                NOT R2, R2
                ADD R2, R2, #1 

                ;Check for 'Q'
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_Q

                ;Check for 'q'
                ADD R2, R2, R4
                ADD R1, R0, R2
                BRnp #1
                JSR STATE_Q

                JSR STATE_FAIL




CHECK_A         ;Turning R2 to a negative number        
                LD R2, A
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'A'
                ADD R1, R0, R2
                BRnp CHECK_a
                RET

CHECK_a         ;Check for 'a'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_B         ;Turning R2 to a negative number        
                LD R2, B
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'B'
                ADD R1, R0, R2
                BRnp CHECK_b
                RET

CHECK_b         ;Check for 'b'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_D         ;Turning R2 to a negative number        
                LD R2, D
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'D'
                ADD R1, R0, R2
                BRnp CHECK_d
                RET

CHECK_d         ;Check for 'd'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_E         ;Turning R2 to a negative number        
                LD R2, E
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'E'
                ADD R1, R0, R2
                BRnp CHECK_e
                RET

CHECK_e         ;Check for 'e'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_I         ;Turning R2 to a negative number        
                LD R2, I
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'I'
                ADD R1, R0, R2
                BRnp CHECK_i
                RET

CHECK_i         ;Check for 'i'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_J         ;Turning R2 to a negative number        
                LD R2, J
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'J'
                ADD R1, R0, R2
                BRnp CHECK_j
                RET

CHECK_j         ;Check for 'j'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_L         ;Turning R2 to a negative number        
                LD R2, L
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'L'
                ADD R1, R0, R2
                BRnp CHECK_l
                RET

CHECK_l         ;Check for 'l'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_M         ;Turning R2 to a negative number        
                LD R2, M
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'M'
                ADD R1, R0, R2
                BRnp CHECK_m
                RET

CHECK_m         ;Check for 'm'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_N         ;Turning R2 to a negative number        
                LD R2, N
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'N'
                ADD R1, R0, R2
                BRnp CHECK_n
                RET

CHECK_n         ;Check for 'n'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_O         ;Turning R2 to a negative number        
                LD R2, O
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'O'
                ADD R1, R0, R2
                BRnp CHECK_o
                RET

CHECK_o         ;Check for 'o'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_P         ;Turning R2 to a negative number        
                LD R2, P
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'P'
                ADD R1, R0, R2
                BRnp CHECK_p
                RET

CHECK_p         ;Check for 'p'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_R         ;Turning R2 to a negative number        
                LD R2, R
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'R'
                ADD R1, R0, R2
                BRnp CHECK_r
                RET

CHECK_r         ;Check for 'r'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_S         ;Turning R2 to a negative number        
                LD R2, S
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'S'
                ADD R1, R0, R2
                BRnp CHECK_s
                RET

CHECK_s         ;Check for 's'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_T         ;Turning R2 to a negative number        
                LD R2, T
                NOT R2, R2
                ADD R2, R2, #1

                ; Check for 'T'
                ADD R1, R0, R2
                BRnp CHECK_t
                RET

CHECK_t         ;Check for 't'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_V         ;Turning R2 to a negative number
                LD R2, V
                NOT R2, R2
                ADD R2, R2, #1

                ;Check for 'V'
                ADD R1, R0, R2
                BRnp CHECK_v
                RET

CHECK_v         ;Check for 't'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

CHECK_ENTER     ;Turning R2 to a negative number
                LD R2, ENTER
                NOT R2, R2
                ADD R2, R2, #1

                ;Check for 'ENTER' key
                ADD R1, R0, R2
                RET

CHECK_Q         ;Turning R2 to a negative number
                LD R2, Q
                NOT R2, R2
                ADD R2, R2, #1

                ;Check for 'Q'
                ADD R1, R0, R2
                BRnp CHECK_q
                RET

CHECK_q         ;Check for 'q'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

                .FILL U
CHECK_U         ;Turning R2 to a negative number
                LDI R2, #-2
                NOT R2, R2
                ADD R2, R2, #1

                ;Check for 'Q'
                ADD R1, R0, R2
                BRnp CHECK_u
                RET

CHECK_u         ;Check for 'q'
                ADD R2, R2, R4
                ADD R1, R0, R2
                RET

                
STATE_A         GETC ;Puts next letter in R0
                
                JSR CHECK_D
                BRz STATE_AD

                JSR CHECK_N
                BRz STATE_AN

                JSR STATE_FAIL

STATE_AD        GETC ;Puts next letter in R0
                JSR CHECK_D
                BRz STATE_ADD
                JSR STATE_FAIL

                .FILL ADD_OP
STATE_ADD       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_ADD
                LDI R0, #-5
                PUTS
                JSR START
FAIL_ADD        JSR STATE_FAIL


STATE_AN        GETC ;Puts next letter in R0
                JSR CHECK_D
                BRz STATE_AND
                JSR STATE_FAIL

                .FILL AND_OP                
STATE_AND       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_AND
                LDI R0, #-5
                PUTS
                JSR START
FAIL_AND        JSR STATE_FAIL

STATE_B         GETC ;Puts next letter in R0

                JSR CHECK_R
                BRz STATE_BR

                JSR STATE_FAIL
                
                .FILL TEMP_OP
STATE_BR        GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_BR
                LDI R0, #-5
                PUTS
                JSR START
FAIL_BR         JSR STATE_FAIL

STATE_J         GETC ;Puts next letter in R0

                JSR CHECK_M
                BRz STATE_JM

                JSR CHECK_S
                BRz STATE_JS

                JSR STATE_FAIL

STATE_JM        GETC ;Puts next letter in R0

                JSR CHECK_P
                BRz STATE_JMP

                JSR STATE_FAIL

                .FILL JMP_OP
STATE_JMP       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_JMP
                LDI R0, #-5
                PUTS
                JSR START
FAIL_JMP        JSR STATE_FAIL

STATE_JS        GETC ;Puts next letter in R0
                JSR CHECK_R
                BRz STATE_JSR
                JSR STATE_FAIL

                .FILL JSR_OP
STATE_JSR       GETC ;Puts next letter in R0
                JSR CHECK_R
                BRz STATE_JSRR
                JSR CHECK_ENTER
                BRnp FAIL_JSR
                LDI R0, #-7
                PUTS
                JSR START
FAIL_JSR        JSR STATE_FAIL

                .FILL JSRR_OP
STATE_JSRR      GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_JSRR
                LDI R0, #-5
                PUTS
                JSR START
FAIL_JSRR       JSR STATE_FAIL

STATE_L         GETC ;Puts next letter in R0

                JSR CHECK_D
                BRz STATE_LD

                JSR CHECK_E
                BRz STATE_LE

                JSR STATE_FAIL

                .FILL LD_OP
STATE_LD        GETC ;Puts next letter in R0

                JSR CHECK_I
                BRz STATE_LDI

                JSR CHECK_R
                BRz STATE_LDR

                JSR CHECK_ENTER
                BRnp FAIL_LD
                LDI R0, #-9
                PUTS
                JSR START
FAIL_LD         JSR STATE_FAIL

                .FILL LDI_OP
STATE_LDI       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_LDI
                LDI R0, #-5
                PUTS
                JSR START
FAIL_LDI        JSR STATE_FAIL

                .FILL LDR_OP
STATE_LDR       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_LDR
                LDI R0, #-5
                PUTS
                JSR START
FAIL_LDR        JSR STATE_FAIL

STATE_LE        GETC ;Puts next letter in R0

                JSR CHECK_A
                BRz STATE_LEA

                JSR STATE_FAIL

                .FILL LEA_OP
STATE_LEA       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_LEA
                LDI R0, #-5
                PUTS
                JSR START
FAIL_LEA        JSR STATE_FAIL

STATE_N         GETC ;Puts next letter in R0

                JSR CHECK_O
                BRz STATE_NO

                JSR STATE_FAIL

STATE_NO        GETC ;Puts next letter in R0

                JSR CHECK_T
                BRz STATE_NOT

                JSR STATE_FAIL

                .FILL NOT_OP
STATE_NOT       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_NOT
                LDI R0, #-5
                PUTS
                JSR START
FAIL_NOT        JSR STATE_FAIL

STATE_R         GETC ;Puts next letter in R0

                JSR CHECK_E
                BRz STATE_RE

                JSR CHECK_T
                BRz STATE_RT

                JSR STATE_FAIL

STATE_RE        GETC ;Puts next letter in R0

                JSR CHECK_T
                BRz STATE_RET

                JSR CHECK_S
                BRz STATE_RES

                JSR STATE_FAIL

                .FILL RET_OP
STATE_RET       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_RET
                LDI R0, #-5
                PUTS
                JSR START
FAIL_RET        JSR STATE_FAIL

STATE_RT        GETC ;Puts next letter in R0

                JSR CHECK_I
                BRz STATE_RTI

                JSR STATE_FAIL

                .FILL RTI_OP
STATE_RTI       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_RTI
                LDI R0, #-5
                PUTS
                JSR START
FAIL_RTI        JSR STATE_FAIL

STATE_S         GETC ;Puts next letter in R0

                JSR CHECK_T
                BRz STATE_ST

                JSR STATE_FAIL

                .FILL ST_OP
STATE_ST        GETC ;Puts next letter in R0

                JSR CHECK_I
                BRz STATE_STI

                JSR CHECK_R
                BRz STATE_STR

                JSR CHECK_ENTER
                BRnp FAIL_ST
                LDI R0, #-9
                PUTS
                JSR START
FAIL_ST         JSR STATE_FAIL

                .FILL STI_OP
STATE_STI       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_STI
                LDI R0, #-5
                PUTS
                JSR START
FAIL_STI        JSR STATE_FAIL

                .FILL STR_OP
STATE_STR       GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_STR
                LDI R0, #-5
                PUTS
                JSR START
FAIL_STR        JSR STATE_FAIL

STATE_T         GETC ;Puts next letter in R0

                JSR CHECK_R
                BRz STATE_TR

                JSR STATE_FAIL

STATE_TR         GETC ;Puts next letter in R0

                JSR CHECK_A
                BRz STATE_TRA

                JSR STATE_FAIL

STATE_TRA       GETC ;Puts next letter in R0

                JSR CHECK_P
                BRz STATE_TRAP

                JSR STATE_FAIL

                .FILL TRAP_OP
STATE_TRAP      GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_TRAP
                LDI R0, #-5
                PUTS
                JSR START
FAIL_TRAP       JSR STATE_FAIL

STATE_RES       GETC ;Puts next letter in R0

                JSR CHECK_E
                BRz STATE_RESE

                JSR STATE_FAIL

STATE_RESE      GETC ;Puts next letter in R0

                JSR CHECK_R
                BRz STATE_RESER

                JSR STATE_FAIL

STATE_RESER     GETC ;Puts next letter in R0

                JSR CHECK_V
                BRz STATE_RESERV

                JSR STATE_FAIL

STATE_RESERV    GETC ;Puts next letter in R0

                JSR CHECK_E
                BRz STATE_RESERVE

                JSR STATE_FAIL

STATE_RESERVE   GETC ;Puts next letter in R0

                JSR CHECK_D
                BRz STATE_RESERVED

                JSR STATE_FAIL

                .FILL RESERVED_OP
STATE_RESERVED  GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_RESEVERED
                LDI R0, #-5
                PUTS
                JSR START
FAIL_RESEVERED  JSR STATE_FAIL

STATE_Q         GETC ;Puts next letter in R0

                JSR CHECK_U
                BRz STATE_QU

                JSR STATE_FAIL

STATE_QU        GETC ;Puts next letter in R0

                JSR CHECK_I
                BRz STATE_QUI

                JSR STATE_FAIL


STATE_QUI       GETC ;Puts next letter in R0

                JSR CHECK_T
                BRz STATE_QUIT

                JSR STATE_FAIL


STATE_QUIT      GETC ;Puts next letter in R0
                JSR CHECK_ENTER
                BRnp FAIL_QUIT

                JSR QUIT
FAIL_QUIT       JSR STATE_FAIL


STATE_FAIL      ADD R1, R1, #0 ;FILLER INSTRUCTION, CAN DELETE
WAIT            GETC
                JSR CHECK_ENTER
                BRnp WAIT
                LD R0, FAILED_STRING
                PUTS
                JSR START



FAILED          .STRINGZ "Input a correct command or quit"
FAILED_STRING   .FILL FAILED
QUIT            HALT
                .END    ; End Program
