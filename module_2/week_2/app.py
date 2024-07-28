import cv2

from background_subtraction import replace_background
from constants import DATA_DIRECTORY_PATH

# The original background image.
original_background_image = cv2.imread(
    f"{DATA_DIRECTORY_PATH}/data/module2_week2_GreenBackground.png", 1
)
original_background_image = cv2.resize(original_background_image, (678, 381))

# The object image with the original background.
object_image = cv2.imread(f"{DATA_DIRECTORY_PATH}/data/module2_week2_Object.png", 1)
object_image = cv2.resize(object_image, (678, 381))

# The new background image.
new_background_image = cv2.imread(
    f"{DATA_DIRECTORY_PATH}/data/module2_week2_NewBackground.jpg", 1
)
new_background_image = cv2.resize(new_background_image, (678, 381))

# The fullname path of the result image.
output_filename_path = f"{DATA_DIRECTORY_PATH}/module_2/week_2/image/output.jpg"

if __name__ == "__main__":
    output_image = replace_background(
        original_background_image, new_background_image, object_image
    )
    cv2.imwrite(output_filename_path, output_image)
    cv2.imshow("Output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
