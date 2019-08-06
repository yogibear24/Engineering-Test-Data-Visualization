import numpy as np
import matplotlib.pyplot as plt
#from scipy.signal import savgol_filter
# DO NOT use Savgol Filter! Since it only applies a polynomial fit, but a stress-strain curve has both a linear portion and a non-linear portion
from scipy.signal import lfilter
# Practice plotting and statistical analysis on a small dataset

def parse_puncture_data(thickness, file_name):
    with open(file_name, "r") as stuff_written_1:
        in_sequence = False
        elapsed_time_list = []
        peak_force_list = []
        for line in stuff_written_1:
            if "Time,Elapsed Time(sec)" in line:
                in_sequence = True
            elif in_sequence is True and line.startswith("20"):
                elapsed_time_list.append(round(float(line.split(',')[1].strip(" ")), 4))
                peak_force_list.append(round(float(line.split(',')[2].strip(" ")), 4))
        elapsed_time_array = np.asarray(elapsed_time_list)
        peak_force_array = np.asarray(peak_force_list)
    return(thickness, elapsed_time_array, peak_force_array)

recipe_one_trial_one_thickness, recipe_one_trial_one_time, recipe_one_trial_one_force = parse_puncture_data(6.29, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_1.CSV")
recipe_one_trial_two_thickness, recipe_one_trial_two_time, recipe_one_trial_two_force = parse_puncture_data(4.15, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_2.CSV")
recipe_one_trial_three_thickness, recipe_one_trial_three_time, recipe_one_trial_three_force = parse_puncture_data(7.00, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_3.CSV")
recipe_one_trial_four_thickness, recipe_one_trial_four_time, recipe_one_trial_four_force = parse_puncture_data(3.72, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_4.CSV")
recipe_one_trial_five_thickness, recipe_one_trial_five_time, recipe_one_trial_five_force = parse_puncture_data(4.22, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_5.CSV")
recipe_one_trial_six_thickness, recipe_one_trial_six_time, recipe_one_trial_six_force = parse_puncture_data(2.98, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_6.CSV")
recipe_one_trial_seven_thickness, recipe_one_trial_seven_time, recipe_one_trial_seven_force = parse_puncture_data(4.49, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_1_Trial_7.CSV")

recipe_three_trial_one_thickness, recipe_three_trial_one_time, recipe_three_trial_one_force = parse_puncture_data(8.39, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_3_Trial_1.CSV")
recipe_three_trial_two_thickness, recipe_three_trial_two_time, recipe_three_trial_two_force = parse_puncture_data(10.04, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_3_Trial_2.CSV")
recipe_three_trial_three_thickness, recipe_three_trial_three_time, recipe_three_trial_three_force = parse_puncture_data(8.89, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_3_Trial_3.CSV")
recipe_three_trial_four_thickness, recipe_three_trial_four_time, recipe_three_trial_four_force = parse_puncture_data(11.88, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_3_Trial_4.CSV")
recipe_three_trial_five_thickness, recipe_three_trial_five_time, recipe_three_trial_five_force = parse_puncture_data(6.98, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Synthetic_Fat/03292019_Recipe_3_Trial_5.CSV")

right_leg_trial_one_thickness, right_leg_trial_one_time, right_leg_trial_one_force = parse_puncture_data(8, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_1.CSV")
right_leg_trial_two_thickness, right_leg_trial_two_time, right_leg_trial_two_force = parse_puncture_data(4.5, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_2.CSV")
right_leg_trial_three_thickness, right_leg_trial_three_time, right_leg_trial_three_force = parse_puncture_data(14.2, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_3.CSV")
right_leg_trial_four_thickness, right_leg_trial_four_time, right_leg_trial_four_force = parse_puncture_data(6.2, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_4.CSV")
right_leg_trial_five_thickness, right_leg_trial_five_time, right_leg_trial_five_force = parse_puncture_data(11.3, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_5.CSV")
right_leg_trial_six_thickness, right_leg_trial_six_time, right_leg_trial_six_force = parse_puncture_data(6.7, "C:/Users/Everet/Documents/CREST/Puncture_Testing/Right_Leg_Fat/04032019_Right_Leg_Trial_6.CSV")

def parse_uniaxial_data(thickness, width, length, file_name):
    with open(file_name, "r") as stuff_written_1:
        in_sequence = False
        points_file_one = []
        elapsed_time_file_one = []
        scan_time_file_one = []
        displace_one_file_one = []
        load_one_file_one = []
        load_two_file_one = []
        displace_e_file_one = []
        # points are unitless, elapsed time and scan time units are seconds, display one and display e units are mm, load one and load two units are Newtons
        for line in stuff_written_1:
            if "Counts,1" in line:
                in_sequence = True
            elif in_sequence is True and line.startswith("    "):
                points_file_one.append(round(float(line.split(',')[0].strip(" ")), 4))
                elapsed_time_file_one.append(round(float(line.split(',')[1].strip(" ")), 4))
                scan_time_file_one.append(round(float(line.split(',')[2].strip(" ")), 4))
                displace_one_file_one.append(round(float(line.split(',')[3].strip(" ")), 4))
                load_one_file_one.append(round(float(line.split(',')[4].strip(" ")), 4))
                load_two_file_one.append(round(float(line.split(',')[5].strip(" ")), 4))
                displace_e_file_one.append(round(float(line.split(',')[6].strip(" ")), 4))
        load_two_file_one_array = np.asarray(load_two_file_one)
        displace_e_file_one_array = np.asarray(displace_e_file_one)
        area_one = (thickness * 10**-3) * (width * 10**-3)
        stress_one = (load_two_file_one_array / area_one) * 10**-3
        strain_one = displace_e_file_one_array / length
        n = 30
        b = [1.0 / n] * n
        a = 1
        filtered_stress_one = lfilter(b, a, ((load_two_file_one_array / area_one) * 10**-3))
        filtered_strain_one = lfilter(b, a, (displace_e_file_one_array / length))
    return(stress_one, strain_one, filtered_stress_one, filtered_strain_one)

recipe_one_trial_one_stress, recipe_one_trial_one_strain, recipe_one_trial_one_stress_f, recipe_one_trial_one_strain_f = parse_uniaxial_data(3.813, 3.856, 30.86, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_1_Trial_1 03072019 031925_tdf.CSV")
recipe_one_trial_two_stress, recipe_one_trial_two_strain, recipe_one_trial_two_stress_f, recipe_one_trial_two_strain_f = parse_uniaxial_data(3.116, 5.107, 28.80, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_1_Trial_2 03072019 033741_tdf.CSV")
recipe_one_trial_three_stress, recipe_one_trial_three_strain, recipe_one_trial_three_stress_f, recipe_one_trial_three_strain_f = parse_uniaxial_data(3.146, 2.034, 41.67, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_1_Trial_3 03072019 035704_tdf.CSV")
recipe_one_trial_four_stress, recipe_one_trial_four_strain, recipe_one_trial_four_stress_f, recipe_one_trial_four_strain_f = parse_uniaxial_data(2.395, 3.743, 34.99, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_1_Trial_4 03072019 041015_tdf.CSV")
recipe_one_trial_five_stress, recipe_one_trial_five_strain, recipe_one_trial_five_stress_f, recipe_one_trial_five_strain_f = parse_uniaxial_data(2.604, 5.015, 31.35, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_1_Trial_5 03072019 042608_tdf.CSV")
recipe_one_trial_six_stress, recipe_one_trial_six_strain, recipe_one_trial_six_stress_f, recipe_one_trial_six_strain_f = parse_uniaxial_data(3.017, 6.781, 30.31, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_1_Trial_6 03262019 023929_tdf.CSV")
recipe_one_trial_seven_stress, recipe_one_trial_seven_strain, recipe_one_trial_seven_stress_f, recipe_one_trial_seven_strain_f = parse_uniaxial_data(2.181, 3.702, 28.38, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_1_Trial_7 03262019 025357_tdf.CSV")
recipe_one_trial_eight_stress, recipe_one_trial_eight_strain, recipe_one_trial_eight_stress_f, recipe_one_trial_eight_strain_f = parse_uniaxial_data(3.598, 4.599, 26.24, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_1_Trial_8 03262019 030815_tdf.CSV")
recipe_one_trial_nine_stress, recipe_one_trial_nine_strain, recipe_one_trial_nine_stress_f, recipe_one_trial_nine_strain_f = parse_uniaxial_data(5.919, 5.738, 26.37, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_1_Trial_9 03262019 032348_tdf.CSV")

recipe_three_trial_one_stress, recipe_three_trial_one_strain, recipe_three_trial_one_stress_f, recipe_three_trial_one_strain_f = parse_uniaxial_data(3.066, 3.742, 43.77, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_3_Trial_1 03072019 044354_tdf.CSV")
recipe_three_trial_three_stress, recipe_three_trial_three_strain, recipe_three_trial_three_stress_f, recipe_three_trial_three_strain_f = parse_uniaxial_data(5.170, 7.726, 30.33, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_3_Trial_3 03072019 051453_tdf.CSV")
recipe_three_trial_four_stress, recipe_three_trial_four_strain, recipe_three_trial_four_stress_f, recipe_three_trial_four_strain_f = parse_uniaxial_data(2.340, 4.246, 40.20, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_3_Trial_4 03072019 053133_tdf.CSV")
recipe_three_trial_five_stress, recipe_three_trial_five_strain, recipe_three_trial_five_stress_f, recipe_three_trial_five_strain_f = parse_uniaxial_data(4.357, 6.285, 32.3, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/030719_Recipe_3_Trial_5 03072019 054828_tdf.CSV")
recipe_three_trial_six_stress, recipe_three_trial_six_strain, recipe_three_trial_six_stress_f, recipe_three_trial_six_strain_f = parse_uniaxial_data(3.875, 5.189, 25.15, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_6 03262019 033931_tdf.CSV")
recipe_three_trial_seven_stress, recipe_three_trial_seven_strain, recipe_three_trial_seven_stress_f, recipe_three_trial_seven_strain_f = parse_uniaxial_data(3.321, 5.097, 26.09, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_7 03262019 035629_tdf.CSV")
recipe_three_trial_eight_stress, recipe_three_trial_eight_strain, recipe_three_trial_eight_stress_f, recipe_three_trial_eight_strain_f = parse_uniaxial_data(3.011, 4.761, 28.73, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_8 03262019 041121_tdf.CSV")
recipe_three_trial_nine_stress, recipe_three_trial_nine_strain, recipe_three_trial_nine_stress_f, recipe_three_trial_nine_strain_f = parse_uniaxial_data(3.993, 6.676, 25.35, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_9 03262019 042530_tdf.CSV")
recipe_three_trial_ten_stress, recipe_three_trial_ten_strain, recipe_three_trial_ten_stress_f, recipe_three_trial_ten_strain_f = parse_uniaxial_data(4.003, 5.802, 29.46, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_10 03262019 044037_tdf.CSV")
recipe_three_trial_eleven_stress, recipe_three_trial_eleven_strain, recipe_three_trial_eleven_stress_f, recipe_three_trial_eleven_strain_f = parse_uniaxial_data(3.188, 5.783, 27.26, "C:/Users/Everet/Documents/CREST/Uniaxial_Testing/Synthetic_Fat/03252019_Recipe_3_Trial_11 03262019 045339_tdf.CSV")


def plot_asethetic_parameters():
    plt.tight_layout(pad=0.4)
    plt.tick_params(axis="x", labelsize=8, pad=0.4)
    plt.tick_params(axis="y", labelsize=8, pad=0.4)

plt.subplot2grid((4,2), (0,0))
plot_asethetic_parameters()
plt.ylabel("Puncture\nForce (N)", fontsize = 8)
plt.xlabel("Time Elapsed (s)", fontsize = 8)
plt.title("Puncture Forces of Synthetic Recipes\nand Real Human Tissues", fontsize = 9)

plt.plot(recipe_one_trial_one_time, recipe_one_trial_one_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_two_time, recipe_one_trial_two_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_three_time, recipe_one_trial_three_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_four_time, recipe_one_trial_four_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_five_time, recipe_one_trial_five_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_six_time, recipe_one_trial_six_force, linewidth = 0.4, color = "b")
plt.plot(recipe_one_trial_seven_time, recipe_one_trial_seven_force, linewidth = 0.4, color = "b")

plt.plot(recipe_three_trial_one_time, recipe_three_trial_one_force, linewidth = 0.4, color = "g")
plt.plot(recipe_three_trial_two_time, recipe_three_trial_two_force, linewidth = 0.4, color = "g")
plt.plot(recipe_three_trial_three_time, recipe_three_trial_three_force, linewidth = 0.4, color = "g")
plt.plot(recipe_three_trial_four_time, recipe_three_trial_four_force, linewidth = 0.4, color = "g")
plt.plot(recipe_three_trial_five_time, recipe_three_trial_five_force, linewidth = 0.4, color = "g")

plt.plot(right_leg_trial_one_time, right_leg_trial_one_force, linewidth = 0.4, color = "r")
plt.plot(right_leg_trial_two_time, right_leg_trial_two_force, linewidth = 0.4, color = "r")
plt.plot(right_leg_trial_three_time, right_leg_trial_three_force, linewidth = 0.4, color = "r")
plt.plot(right_leg_trial_four_time, right_leg_trial_four_force, linewidth = 0.4, color = "r")
plt.plot(right_leg_trial_five_time, right_leg_trial_five_force, linewidth = 0.4, color = "r")
plt.plot(right_leg_trial_six_time, right_leg_trial_six_force, linewidth = 0.4, color = "r")
#plt.legend(loc = "upper right")

plt.subplot2grid((4,2), (0,1))
plot_asethetic_parameters()
plt.ylabel("Puncture Force per\nThickness Ratio (F / mm)", fontsize = 8)
plt.title("Puncture Force per Thickness\nRatio of Various Tissues", fontsize = 9)

recipe_one_max_force_list = [max(recipe_one_trial_one_force) / recipe_one_trial_one_thickness, max(recipe_one_trial_two_force) / recipe_one_trial_two_thickness,
                             max(recipe_one_trial_three_force) / recipe_one_trial_three_thickness, max(recipe_one_trial_four_force) / recipe_one_trial_four_thickness,
                             max(recipe_one_trial_five_force) / recipe_one_trial_five_thickness, max(recipe_one_trial_six_force) / recipe_one_trial_six_thickness,
                             max(recipe_one_trial_seven_force) / recipe_one_trial_seven_thickness]
recipe_three_max_force_list = [max(recipe_three_trial_one_force) / recipe_three_trial_one_thickness, max(recipe_three_trial_two_force) / recipe_three_trial_two_thickness,
                               max(recipe_three_trial_three_force) / recipe_three_trial_three_thickness, max(recipe_three_trial_four_force) / recipe_three_trial_four_thickness,
                               max(recipe_three_trial_five_force) / recipe_three_trial_five_thickness]
right_leg_max_force_list = [max(right_leg_trial_one_force) / right_leg_trial_one_thickness, max(right_leg_trial_two_force) / right_leg_trial_two_thickness,
                             max(right_leg_trial_three_force) / right_leg_trial_three_thickness, max(right_leg_trial_four_force) / right_leg_trial_four_thickness,
                             max(right_leg_trial_five_force) / right_leg_trial_five_thickness, max(right_leg_trial_six_force) / right_leg_trial_six_thickness]
list_of_max_force_lists = [recipe_one_max_force_list, recipe_three_max_force_list, right_leg_max_force_list]
plt.boxplot(list_of_max_force_lists, labels = ["Recipe 1", "Recipe 3", "Human\nTissue"])


plt.subplot2grid((4,2), (1,0), colspan = 2)
plot_asethetic_parameters()
plt.ylabel("Recipe One\nStress (kPa)", fontsize = 8)
plt.xlabel("Recipe One Strain", fontsize = 8)
plt.title("Stress-Strain Behavior of Synthetic Tissue Recipe One", fontsize = 9)

plt.plot(recipe_one_trial_one_strain, recipe_one_trial_one_stress, linewidth = 0.4, color = "b", label = "Trial 1")
plt.plot(recipe_one_trial_two_strain, recipe_one_trial_two_stress, linewidth = 0.4, color = "tab:orange", label = "Trial 2")
plt.plot(recipe_one_trial_three_strain, recipe_one_trial_three_stress, linewidth = 0.4, color = "tab:green", label = "Trial 3")
plt.plot(recipe_one_trial_four_strain, recipe_one_trial_four_stress, linewidth = 0.4, color = "tab:red", label = "Trial 4")
plt.plot(recipe_one_trial_five_strain, recipe_one_trial_five_stress, linewidth = 0.4, color = "tab:olive", label = "Trial 5")
plt.plot(recipe_one_trial_six_strain, recipe_one_trial_six_stress, linewidth = 0.4, color = "m", label = "Trial 6")
plt.plot(recipe_one_trial_seven_strain, recipe_one_trial_seven_stress, linewidth = 0.4, color = "tab:purple", label = "Trial 7")
plt.plot(recipe_one_trial_eight_strain, recipe_one_trial_eight_stress, linewidth = 0.4, color = "tab:pink", label = "Trial 8")
plt.plot(recipe_one_trial_nine_strain, recipe_one_trial_nine_stress, linewidth = 0.4, color = "tab:cyan", label = "Trial 9")


plt.subplot2grid((4,2), (2,0), colspan = 2)
plot_asethetic_parameters()
plt.ylabel("Recipe Three\nStress (kPa)", fontsize = 8)
plt.xlabel("Recipe Three Strain", fontsize = 8)
plt.title("Stress-Strain Behavior of Synthetic Tissue Recipe Three", fontsize = 9)

plt.plot(recipe_three_trial_one_strain, recipe_three_trial_one_stress, linewidth = 0.4, color = "tab:olive", label = "Trial 1")
# Trial 2 left out because failed early, during preconditioning
plt.plot(recipe_three_trial_three_strain, recipe_three_trial_three_stress, linewidth = 0.4, color = "tab:orange", label = "Trial 3")
#plt.plot(recipe_three_trial_four_strain, recipe_three_trial_four_stress, linewidth = 0.4)
# Bad Data, almost no stress or strain data at all
plt.plot(recipe_three_trial_five_strain, recipe_three_trial_five_stress, linewidth = 0.4, color = "tab:green", label = "Trial 5")
plt.plot(recipe_three_trial_six_strain, recipe_three_trial_six_stress, linewidth = 0.4, color = "tab:red", label = "Trial 6")
plt.plot(recipe_three_trial_seven_strain, recipe_three_trial_seven_stress, linewidth = 0.4, color = "b", label = "Trial 7")
plt.plot(recipe_three_trial_eight_strain, recipe_three_trial_eight_stress, linewidth = 0.4, color = "m", label = "Trial 8")
plt.plot(recipe_three_trial_nine_strain, recipe_three_trial_nine_stress, linewidth = 0.4, color = "tab:grey", label = "Trial 9")
plt.plot(recipe_three_trial_ten_strain, recipe_three_trial_ten_stress, linewidth = 0.4, color = "tab:cyan", label = "Trial 10")
plt.plot(recipe_three_trial_eleven_strain, recipe_three_trial_eleven_stress, linewidth = 0.4, color = "tab:pink", label = "Trial 11")


plt.subplot2grid((4,2), (3,0), colspan = 2)
plot_asethetic_parameters()
plt.ylabel("Synthetic Tissue\nStress (kPa)", fontsize = 8)
plt.title("Fracture Stresses of Various Synthetic Tissue Recipes", fontsize = 9)

recipe_one_stress_list = [max(recipe_one_trial_one_stress_f), max(recipe_one_trial_two_stress_f), max(recipe_one_trial_three_stress_f), max(recipe_one_trial_four_stress_f), max(recipe_one_trial_five_stress_f),
                          max(recipe_one_trial_six_stress_f), max(recipe_one_trial_eight_stress_f), max(recipe_one_trial_nine_stress_f)]
recipe_three_stress_list = [max(recipe_three_trial_one_stress_f), max(recipe_three_trial_three_stress_f), max(recipe_three_trial_five_stress_f), max(recipe_three_trial_six_stress_f), max(recipe_three_trial_seven_stress_f),
                            max(recipe_three_trial_eight_stress_f), max(recipe_three_trial_nine_stress_f), max(recipe_three_trial_ten_stress_f), max(recipe_three_trial_eleven_stress_f)]
list_of_stress_arrays = [recipe_one_stress_list, recipe_three_stress_list]
plt.boxplot(list_of_stress_arrays, labels = ["Recipe 1", "Recipe 3"])

plt.show()
