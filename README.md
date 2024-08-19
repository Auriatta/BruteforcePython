The main function is to break(but not really..) 2d num pads using mouse simulation for that.

Main Features:
- Simulating and receiving mouse and keyboard input (Pynput lib)
- Pin generating algorithm

Issues:
Code can't handle exiting while generating PIN code using keyboard command (Down).
Can be fixed tho by implementing async thread ability using asyncio library.

<br />
The user had to define how many digits has the PIN code and from which value it should start.
After running it, the user needs to input the position of the curtain num pad digits.
Then using the UP key, the user can start breaking the PIN Code.

The BruteForceDigitsGenerator is responsible for generating PIN codes with array output and inheriting the class BruteForceNumpadMouseInput for input simulation.

The PIN code generator is based on incrementing value and moving its digits into slots replacing by that: zeros.
 
For separate digits, its uses a nonmodulo math formula that I have created for porpuse of this code:    
<br />$\rfloor(  \frac{a - \rfloor(\frac{a}{10^b} * 10^b) }{ 10 ^ c } )$<br />    
Where:  
$a =$ value  
$i =$ digit index  
$b = n - i$  
$c = b - 1$  
$n = log10(a)+1$  

![image](https://github.com/user-attachments/assets/60e33a4d-9f7c-4c7b-8d4b-d99f1d6201a2)

I have approached this as instructions. First I have removed left side digits from $a$. Moved coma by /10^b and floor the result to cut. I had to perform the cut before the index that contained the wanted digit. For that, I had to know how to calculate the number of digits, which formula I found in the internet ($log10(a)+1$). The question was, what to do next? I have a value of a few first digits of $a$. I've powered the value by 10^b so it could contain the same amount of zeros as several digits that have been cut and subtract the acquired value from $a$. Now I have the right side. Only need all digits but not the first one, to be removed. To do this used the same method as with getting the left side but this time I had to spare one comma for the wanted digit: 10^c.
