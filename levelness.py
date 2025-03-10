import interface2

category1 = None
category = None
category_thickness = None
verage_angle = None
std_dev_thickness = None
std_dev = None
probabilities = None
average_angle = None
result_tesseract = None
image_tesseract = None
image_path = None
text = ''
from interface2 import upload
#variable = None

def predictnow(variable, locker):

    global category1
    global category
    global category_thickness
    global verage_angle
    global std_dev_thickness
    global std_dev
    global probabilities
    global average_angle
    global result_tesseract
    global image_tesseract
    global image_path
    global text

    import paddleocr
    from fire.console import files
    from paddleocr import PaddleOCR, draw_ocr
    import cv2
    from PIL import Image
    import matplotlib.pyplot as plt
    import pytesseract
    import numpy as np
    import matplotlib.patches as patches
    import math
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    # Instantiate an OCR agent
    ocr_agent_paddle = PaddleOCR()
    ocr_agent_tesseract = pytesseract.pytesseract

    # Define the number of strokes for each letter
    strokes = {
        'a': 2,
        'b': 2,
        'd': 2,
        'e': 2,
        'h': 2,
        'l': 1,
        'k': 2,
        'i': 1,
        'm': 2,
        'o': 1,
        'r': 2,
        't': 2,
        'u': 2
    }

    from paddleocr import PaddleOCR, draw_ocr
    import pandas as pd
    import tempfile

    uploaded = 'sz.png'
    def categorize_angle(angle):
        if angle <= 88:
            return 'Ascending'
        elif angle >= 92:
            return 'Descending'
        else:
            return 'Leveled'

    angles = []

    def calculate_word_spacings(boxes):
        spacings = [boxes[i+1][0][0] - boxes[i][2][0] for i in range(len(boxes) - 1)]

        return spacings


    df = pd.DataFrame(columns=['ID', 'BASELINE LBL', 'SPACING LBL', 'THICKNESS LBL','BASELINE', 'THICKNESS','SPACING'])


    try:
        # Read the image

                if variable is not None and locker is False:
                    image_path = variable
                    print("Catch: ", str(image_path))
                else:
                    image_path = 'drawing.jpg'
                    print("current", image_path)

                #image_path = r'C:\Users\Joash\Downloads\fffeee.png'

                img = cv2.imread(image_path)

                # Convert the image to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Apply a blur filter to the image
                #blurred = cv2.GaussianBlur(gray, (9, 3), 0)

                # Apply a binary threshold to the image
                ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

                temp_filename = tempfile.mktemp(suffix='.jpg')
                cv2.imwrite(temp_filename, thresh1)




                # Use the PaddleOCR agent to detect words and strokes
                result_paddle = ocr_agent_paddle.ocr(temp_filename) ##

                # Initialize the total strokes counter
                total_strokes = 0

                # Draw bounding boxes and display the image
                image = cv2.imread(temp_filename) ##
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                boxes = [word_info[0] for line in result_paddle for word_info in line if word_info is not None]
                image = draw_ocr(image, boxes)
                cv2.imwrite("paddleoutput.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                #plt.imshow(image)
                #plt.title("PaddleOCR Detection Results")
                #plt.show()

                print("PaddleOCR Detection Results: ")
                # Check if result is not None
                if result_paddle is not None:

                    # Process the OCR result
                    angles = []
                    for line in result_paddle:

                        # Check if line is not None
                        if line is not None:
                            for word_info in line:

                                # Check if word_info is not None
                                if word_info is not None:
                                    box = np.array(word_info[0])
                                    word = str(word_info[-1])  # Convert to string

                                    # Reset the total strokes counter for each word
                                    total_strokes = 0

                                    # Calculate the angle of the bounding box
                                    dx = box[3][0] - box[0][0]
                                    dy = box[3][1] - box[0][1]
                                    angle = math.degrees(math.atan2(dy, dx))
                                    angles.append(angle)

                                    # Print the angle of the bounding box
                                    print(f"The angle of the bounding box for '{word}' is {angle} degrees.")

                    # Calculate the average angle
                    average_angle = sum(angles) / len(angles)
                    print(f"The average angle is {average_angle} degrees.")

                    # Categorize the average angle
                    category1 = categorize_angle(average_angle)
                    print(f"Your baseline angle is categorized as '{category1}'.")

                    # Calculate the spacings between consecutive bounding boxes
                    spacings = calculate_word_spacings(boxes)
                    print("Spacings between consecutive words:", spacings, '\n')


                # Use the PyTesseract agent to detect individual letters
                result_tesseract = pytesseract.image_to_boxes(cv2.imread(temp_filename))
                # Draw bounding boxes and display the image for PyTesseract
                image_tesseract = cv2.imread(temp_filename) ##
                fig, ax = plt.subplots(1)
                #ax.imshow(image_tesseract)

                for line in result_tesseract.split('\n'):
                    if len(line.split()) == 6:
                        char, x1, y1, x2, y2, _ = line.split()
                        # Calculate letter thickness and spacing
                        spacing = int(y2) - int(y1)
                        thickness = int(x2) - int(x1)
                        # Draw bounding box for each character
                        rect = patches.Rectangle((int(x1), image_tesseract.shape[0] - int(y2)), int(x2) - int(x1), int(y2) - int(y1), linewidth=1, edgecolor='g', facecolor='none')
                        ax.add_patch(rect)

               #cv2.imwrite("tesseractoutput.jpg", cv2.cvtColor(rect, cv2.COLOR_RGB2BGR))
                #plt.title("PyTesseract Detection Results")
                #plt.show()

                print("\nPyTesseract Detection Results: ")


               # Initialize previous x2
                prev_x2 = None

                # Initialize spacings list
                spacings = []
                std_dev = 0
                for line in result_tesseract.split('\n'):
                    if len(line.split()) == 6:
                        char, x1, y1, x2, y2, _ = line.split()

                        # Check if the character is a text character
                        if char.isalpha():
                            # Calculate letter thickness
                            thickness = int(x2) - int(x1)

                            # Calculate spacing
                            if prev_x2 is not None:
                                spacing = abs(int(x1) - prev_x2)  # Use abs() to get the absolute value
                                spacings.append(spacing)  # Add spacing to spacings list
                            else:
                                spacing = 0

                            # Update previous x2
                            prev_x2 = int(x2)

                            print(f"Character: {char}, Thickness: {thickness}, Spacing: {spacing}")
                            print(std_dev)
                            global text
                            text += str(char)


                # Calculate the standard deviation of the spacings
                std_dev = np.std(spacings)

                # Categorize the spacings based on the standard deviation
                if std_dev < 10:
                    category = 'regular'
                elif std_dev < 20:
                    category = 'slightly regular'
                elif std_dev < 30:
                    category = 'less regular'
                else:
                    category = 'not regular'

                print(f"The spacings are {category}.")

                thicknesses = []

                for line in result_tesseract.split('\n'):
                    if len(line.split()) == 6:
                        char, x1, y1, x2, y2, _ = line.split()

                        # Check if the character is a text character
                        if char.isalpha():
                            # Calculate letter thickness
                            thickness = int(x2) - int(x1)
                            thicknesses.append(thickness)  # Add thickness to thicknesses list

                # Calculate the standard deviation of the thicknesses
                std_dev_thickness = np.std(thicknesses)

                # Categorize the thickness based on the standard deviation
                if std_dev_thickness < 10:
                    category_thickness = 'consistent'
                elif std_dev_thickness < 20:
                    category_thickness = 'slightly consistent'
                else:
                    category_thickness = 'not consistent'

                print(f"The thicknesses are {category_thickness}.")

                #df = df.append({'ID': image, 'BASELINE LBL': category1, 'SPACING LBL': category, 'THICKNESS LBL': category_thickness, 'BASELINE':average_angle, 'THICKNESS': std_dev_thickness, 'SPACING':std_dev}, ignore_index=True)
                df.loc[0, 'ID'] = 1
                df.loc[0, 'BASELINE LBL'] = category1
                df.loc[0, 'SPACING LBL'] = category
                df.loc[0, 'THICKNESS LBL'] = category_thickness
                df.loc[0, 'BASELINE'] = average_angle
                df.loc[0, 'THICKNESS'] = std_dev_thickness
                df.loc[0, 'SPACING'] = std_dev
                print("detected: ", text)

    except Exception as e:
                print(f"An error occurred while processing image {1}: {str(e)} 😞 ")
                print("Moving on to the next image...")

    df.head()

    import pandas as pd
    #df = pd.read_csv('/content/LPD.csv')
    irrelevant_columns = ['ID', 'BASELINE LBL', 'SPACING LBL', 'THICKNESS LBL']

    # Drop the irrelevant columns
    df = df.drop(irrelevant_columns, axis=1)


    import pickle

    with open('svm_model (1).pkl', 'rb') as file:
        model = pickle.load(file)

    #new_pred = model.predict(df)
    #print(new_pred)
    probabilities = model.predict_proba(df)
    print(probabilities)
    text = ''


#predictnow(variable, False)
print(category1,
category,
category_thickness,
verage_angle,
std_dev_thickness,
std_dev)