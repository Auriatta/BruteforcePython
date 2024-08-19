The main function is to break(but not really..) 2d num pads using mouse simulation for that.

Main Features:
- Simulating and receiving mouse and keyboard input (Pynput lib)
- Pin generating algorithm
<br />
The user had to define how many digits has the PIN code and from which value it should start.
After running it, the user needs to input the position of the curtain num pad digits.
Then using the UP key, the user can start breaking the PIN Code.

The BruteForceDigitsGenerator is responsible for generating PIN codes with array output and inheriting the class BruteForceNumpadMouseInput for input simulation.

The PIN code generator is based on incrementing value and moving its digits into slots replacing by that: zeros.
 
For separate digits, its uses a nonmodulo math formula:    
<br />$\rfloor(  \frac{a - \rfloor(\frac{a}{10^b} * 10^b) }{ 10 ^ c } )$<br />    
Where:  
$a =$ a value  
$i =$ a digit index  
$b = n - i$  
$c = b - 1$  
$n = log10(a)+1$  

![image](https://github.com/user-attachments/assets/60e33a4d-9f7c-4c7b-8d4b-d99f1d6201a2)
