<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution (INSERT YOUR SCREENSHOT)](screenshots/CREATE_A_SCREENSHOT_OF_YOUR_local_setup.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                       | name          | value                    |
   |----------------------------|---------------|--------------------------|
   | built-in primitive type    | Boolean       | TRUE                     |
   | built-in composite type    | List - Pixels | [O, x, x,x,x,x,...]      |
   | user-defined type          | Class(Smiley) | Instance of Smiley class |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                 | Type                                         |
   |------------------------|----------------------------------------------|
   | sense_hat              | Instance of SenseHat (self.sense_hat)        |
   | pixels                 | List(list of tuples representing RGB values) |
   | WHITE/GREEN/RED/YELLOW | Tuple(RGB values are constant)               |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow  | File      | First line          | Line range |
   |---------------|-----------|---------------------|------------|
   | sequence      | smiley.py | self.pixels = [     | (20 - 29)  |
   | selection     | sad.py    | if wide_open:       | (26 - 29)  |
   | iteration     | happy.py  | for pixel in mouth: | (21 - 22)  |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                     | Used? | Example                                       |
   |--------------------------|-------|-----------------------------------------------|
   | int                      | Yes   | WHITE = (255, 255, 255) from Smiley.py        |
   | float                    | Yes   | delay = 0.25 in happy.py                      |
   | str                      | No    | guess = "money" -> an example                 |
   | bool                     | Yes   | self.draw_eyes(wide_open=False) from happy.py |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> Your answer here
> An example of a class variable in smiley.py is the YELLOW variable in the Smiley class. 
> This is because it is shared by all instances of Smiley class and represents a fixed value
> (RGB colour). Class variables are used for constants or attributes that are the same for 
> every instance. That is what the Smiley class is doing with the RGB values for each child 
> class (Sad, Happy). 
> An example of an instance variable is self.sense_hat which is defined in the __init__ 
> method. Each Smiley instance creates its own SenseHat object meaning that self.sense_hat 
> is unique to each instance. This is important because each Smiley object needs to control 
> their own SenseHat display independently of other Smiley objects. 
> They are differently defined because a class variable is shared across all instances whereas, 
> the instance variable is unique to each object. This is helpful because it allows us to ask 
> for specific behaviours from the data to be tied to the objects individually. 

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Your answer here
   > The purpose of a constructor in general is to set up the initial state of an object. A 
   > constructor is a special method that sets up automatically when an object of a class is 
   > created.
   > The constructor in happy.py in particular is set up initializing the object's 
   > attributes draw_mouth() and draw_eyes(). 

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > Your answer here
   > It executes `self.draw_eyes(wide_open=False)`, `self.show()`, `self.draw_eyes
   > (wide_open=True)` and `self.draw_mouth()` statements and calls methods from the Smiley 
   > parent class and Blinkable abstract class. 
   > The super() function is used to refer to the parent class. 

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   
> Your answer here
>The code styles follows the PEP 8 style guide, which is a standard Python style guide used 
> for writing clean, readable and consistent Python code.  
> Yes it is likely that smiley.py code is using the same code style following PEP 8 because 
> both SenseHat and smiley.py are written in Python and PEP 8 is the widely accepted style 
> guide for Python programming. 
> Another reason is because it is developed and maintained by professional developers and it 
> is Raspberry Pi's Foundation ecosystem it will always aim to set or follow the guidelines 
> for best practices. 


2. List three aspects of this convention you see applied in the code.

> Your answer here
> 1. Proper Indentation : Use of 4-space indentation and no tabs, as per recommended by PEP 8. 
> 2. Naming conventions : Constant such as WHITE,GREEN, RED, YELLOW and BLANK written in all 
     > uppercase letters clearly written as CONSTANTS. 
> 3. Method Naming with Snake Case : using lowercase letters separated by underscores 
     > (snake_case), as recommended by PEP 8 for functions and method names. Example: 
     > (dim_display)

3. Give two examples of organizational documentation in the code.

> Your answer here
> Docstrings: The code uses multi-line docstrings which is an example of organizational 
> documentation for methods to describe their purpose and parameters of method. 
> The format is not fully complete since it's missing some details 
> like :return or :param tags. Docstrings provide basic understanding of what the methods do
> Example of docstring used in smiley.py from line 32: 
> def dim_display(self, dimmed=True): 
> """Set SenseHat's light intensity..."")
> Comments (Inline): Inline comments are present in the code to explain specific sections of 
> what the code is doing. Comments are another example of organizational documentation that 
> help clarify the functionality and purpose of different blocks for readers or other 
> developers. 
> Example of a comment from line 14 from smiley.py : # We have encapsulated the SenseHat object

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s)   |
|------------|---------------|--------------------|
| NotReal    | Sub           | NotRealParent      |
| Smiley     | Super         | No parent          |
| Happy      | Sub           | Smiley, Blinkable  |
| Sad        | Sub           | Smiley             |
| Blinkable  | Super         | ABC abstract class |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Your answer here
> Abstraction is the process of hiding complexity of implemented code. For example, a driver 
> driving a car will see the car as an object with its own unique behaviour. But whatever 
> the complexity is behind driving that car is unknown or hidden from the driver. 
> The implementation of abstraction in Smiley is demonstrated in the Happy class. It has 
> functionality for a happy expression and blinking behaviour but these details of how the 
> Smiley does or displays the pixels of the behaviours are hidden from the user. 
> So when the user is using the blink() method in Happy class and calling it they don't need to 
> understand the internal workings of how the eyes are drawn, updated or display the LED 
> matrix, but we just simply interact and use the blink() method using self.pixels and 
> self.show() to display and update the face. 

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> The process of deriving from base classes is called Inheritance. The derived classes 
> are known as a child class or a subclass which is derived and created from an existing 
> parent class. The purpose of Inheritance is to have easy access for the child class to 
> inherit the methods and attributes of the Base class to reduce repetition 
> and promote code reuse. This helps us use the functionality of the class without 
> duplicating code. 
> In this project, the Happy class demonstrates inheritance by extending the Smiley clss. 
> The Happy class reuses the attributes and methods of Smiley (e.g. self.pixels and show()) 
> while also adding its own functionality like drawing the expression and implementing the 
> blink method from Blinkable. 


### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > First Key difference is one class smiles while the other frowns (pixel formation is 
   > different.)
   > One class(Happy) contains `Blinkable class` imported and passed on as a parameter while 
   > the other does not.
2. What are the key similarities?
   > Both Classes are Child classes of Smiley super.()__init__ method is used 
   > Both Classes have the same functions and instance of the Object of draw_mouth and 
   > draw_eyes e
3. What difference stands out the most to you and why?
   > The Blinkable method stands out the most to me because it is present in the Happy but 
   > not the sad hence giving the Happy class the ability to blink but not the sad class. 
   >
4. How does this difference affect the functionality of these classes
   > The differences affect the functionality of the classes in a minor way. Since they are 
   > both separate classes with separate functions and values if one class is different to 
   > the other it would not make a difference to each other. But not having the ability to 
   > blink for the sad class makes it less functional and behaviour wise it is only frowns. 
   > Whereas the Happy face has some sort of functionality making it more animated. 
   >

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Smiley class, 
   > Sad class and 
   > Happy class
   >
2. Which of these classes directly interact with the SenseHat functionalities?
   > Only Smiley class directly utilizes functionality of the SenseHat using methods like 
   > sense_hat.low_light and sense_hat.set_pixels
   >
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > W
   > In terms of Encapsulation which is the bundling of attributes (data) and methods 
   > (functions) that operate the data into a single unit known as a class. This helps hide 
   > the internal state of an object from the outside world.  
   > Python uses double underscores (__) prefixes to indicate that a method is intended for 
   > internal use within its class and subclasses (private members). Using SenseHAT to
   > hide the methods and attributes within the class unless called access upon to use it for 
   > implementation purpose. For instance in Smiley class we call the SenseHat method self.
   > sense_hat.low_light and the internal working of the class from SenseHat is hidden but 
   > we get to implement the code with the Smiley class within the dim_display function. 
   > This hiding and making things invisible to outside code and reduces risk of making any 
   > accidental data modifications directly to SenseHat class itself and doesn't affect code 
   > uses in the class. 


### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> No, the code's author does not believe that every `Smiley` should be able to blink. 
> If the author intended for all the Smiley objects to have blinking behaviour, the Smiley 
> class itself would have inherited from the Blinkable abstract class. This would help 
> make sure that all subclasses of Smiley, both Happy and Sad would need to implement the 
> blink() method.
> Instead, the current implementation shows that only Happy smiley can blink. It 
> explicitly uses the Blinkable interface and this causes the blinking behaviour which is 
> specific only to Happy class and not for all Smiley objects. For our Sad smiley there is 
> no use or implementation of Blinkable or blink() method hence not all Smiley objects are 
> expected to blink. 
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> No, the author does not expect all Smiley's that blink to blink in the same way. 
> As mentioned if the author intended that all blinking smileys to have the same behaviour 
> then they would've implemented the blink() method as a concrete method in Blinkable 
> abstract class, making sure that all subclasses would inherit this blinking behaviour 
> without needing to redefine it.This means that every blink() method is an 
> abstract method meaning that each subclass implementing Blinkable interface needs to 
> define its own specific behaviour for blinking, for instance  in Happy class we used the blink() 
> method but had to use attributes such as `delay` parameter to control the time of blinking. 
> This design suggests that the author could have wanted the Smileys to behave differently or
> blink however whether it be blinking slowly or blinking frequently.  
> 

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism means many forms. In Python, polymorphism supports defining methods in child classes that override or extend 
> in a parent or abstract class. In the Smiley project, polymorphism is demonstrated with 
> the blink() method. Currently, the Happy and Sad class both have their own versions of the 
> method. Currently, the Happy class uses the bink() method inherited from the Blinkable 
> interface, while the Sad class defines its own blink() method. This allows the blink() 
> method to behave differently depending on the smiley type, making it polymorphic. 
> 

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> The blink method is used in Happy class to make the smiley `blink` this method is 
> inherited from the Blinkable class. Inheritance is important for Polymorphism because 
> Polymorphism can be achieved using the inheritance of a base class, 
> defining a common interface in a base class and then by providing specific implementations 
> in derived classes. In this case blink is inherited and used as methods and modified to 
> return the blink effect with inbuilt import method like time to make the `smiley` face blink.
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](screenshots/sad_blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > Imported time and enhanced the Sad class with blinking functionality by modifying the 
  > draw_eyes method and adding the blink method. Imported the Sad class into main.py, 
  > created an object. And assigned a method to animate the sad smiley's eye-blinking 
  > behaviour. Adjustments ensured smooth transitions and consistent expression rendering. 

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

        > The Blinkable class is an abstract base class(ABC) in Python because it inherits
        > from the ABC class in python. This means it can define abstract methods that must 
        > be implemented by any subclass. Like how in the smiley project it defines abstract 
        > methods related to blinking behaviour, ensuring smiley class like Happy inherits 
        > consistent blinking functionality. 

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.
        > The Blinkable class is designed to be implemented by other classes with no 
        > concrete implementation, is called an abstract class. The generic term being 
        > Abstraction class.

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

        > Abstraction is the OO principle this class represents. This class contains blink 
        > method which is designed to allow child classes to implement its content.
        > It also demonstrates polymorphism since different child classes have different 
        > implementations on blink method showing different behaviours for the same interface. 

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

        > The Blinkable class's `blink` method doesn't have any built-in functionality so 
        > when inheriting from it doesn't automatically make the smiley blink. However,  
        > writing the blink method directly in the Sad class, just like it's done in the Happy 
        > class. This way we don't need to use or inherit the Blinkable class we can just 
        > simply add the blinking feature. 

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

        > The capability is known as Dynamic Typing in Python. Dynamic typing in python is a 
        > core feature that distinguishes it from languages like C#, Java or C++. In a 
        > dynamically typed language the type of variable is determined at runtime meaning we 
        > don't have to explicitly declare variable types, it is inferred when a value is 
        > assigned. In Statically typed languages we need to declare its type for example in C# 
        ```c#
            int x = 10;
            string y = "Hi";
        ```
        > In Python, we can simply assign a value to a variable without specifying the type.
        > Python follows the principle of "Duck typing" this is derived from the term "if it 
        > looks like a duck, swims like a duck and quacks like a duck, then it probably is a 
        > duck". This describes how Python handles object behaviour. It doesn't check an 
        > object's type explicitly. As long as it can perform the actions required.
        ```Python
            x = 10
            y = "Hello" ```
        
  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > Yellow is defined for Happy class. Blue is defined in Sad class. Red is defined 
        > for Anger class and Green is defined in Sick class.
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > These variables are known as Tuples and they are represented and held in RGB 
        > values. Tuples are immutable (non-changeable) hence the colour does not change 
        > while one emotion is running. 
     3. Add the color blue to the appropriate class using the appropriate format and values.
        > Blue has the RGB value of (0, 0, 255)

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > Happy and Sad classes. 

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Easiest way to change the colour would be by rewriting or overwrite the YELLOW value
     > in smiley.py with RGB value for GREEN.  

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
        > Inheritance best applies to the modification made above. 
  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.
        
  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
    super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
