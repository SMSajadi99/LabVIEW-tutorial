# Claculator

In this introductory project, I developed a simple calculator using LabVIEW 2014. The calculator is capable of performing the four basic arithmetic operations: addition, subtraction, multiplication, and division. The front panel of the VI (Virtual Instrument) features two numerical input controls for users to enter the operands, along with four push buttons corresponding to the four operations.


Upon clicking the desired operation button, the calculator executes the respective arithmetic function and displays the result in a numerical indicator on the front panel. The block diagram, which constitutes the program's logic, consists of various LabVIEW nodes and structures wired together to implement the calculator's functionality.


However, during the development process, I encountered one notable challenge:


Lack of Input Validation: The initial version of the calculator did not include input validation mechanisms. Users could enter non-numerical values or invalid characters into the operand input controls, potentially causing runtime errors or producing erroneous results. To address this limitation, I incorporated input validation using the LabVIEW "Scan From String" node, which parses the input strings and ensures that only valid numerical values are accepted for the operands.


Despite these initial challenges, the process of developing this calculator application in LabVIEW 2014 proved to be an invaluable learning experience. It allowed me to familiarize myself with the LabVIEW development environment, understand the concept of data flow programming, and gain hands-on experience with various LabVIEW functions and structures.


Moving forward, I plan to enhance the calculator's functionality by adding support for more advanced operations, implementing a user-friendly interface, and exploring additional features that could improve the overall user experience. The handling of division by zero issue has been successfully addressed, and I look forward to tackling input validation in the next iteration of the project.

Result:


Be happy :)
 
