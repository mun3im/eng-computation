# Code listings from *Engineering Computation with Python*

Every code listing longer than five lines, extracted from the book's LaTeX
source into runnable `.py` files. Generated from edition **J2** (second
edition).

**218 scripts** in 18 folders, named `NN_description.py`,
where `NN` is the order of appearance in the chapter. Each file's docstring
names the chapter and section it came from and, where the book prints one,
the output the book says the code produces. That makes every script
checkable against the book.

The helper modules that the book imports by name are also included, under
those names, so that `from mesh_solver import mesh_solver` and similar imports
work: `constants.py` (ch 3), `math_operations.py` and `my_module.py` (ch 5), `mesh_solver.py` and `greek_conversion.py` (ch 10), `stability_check.py` (ch 13), `datastat_module.py` (ch 14).

## Chapter numbering in J2

The second edition moved machine learning out of Chapter 14 into its own
chapter. Folders follow the J2 book:

| Folder | Chapter |
|---|---|
| `chapter14/` | Engineering Statistics and Data Analysis |
| `chapter15/` | A First Look at Machine Learning (new) |
| `chapter16/` | A First Look at Object-Oriented Python (was `chapter15/`) |

## Running them

```sh
cd scripts/chapter08
python3 04_a_simple_series_circuit.py
```

Plotting listings call `plt.show()`; set `MPLBACKEND=Agg` to run them without
a display. `run_all.py` runs everything and reports:

```sh
python3 scripts/run_all.py            # all chapters
python3 scripts/run_all.py chapter12  # one chapter
```

Some Chapter 10 listings write results back into `tempData.xlsx`,
`tempData.csv` and `circuit_analysis.xlsx`. Keep a clean copy, or restore the
files with `git checkout -- scripts/chapter10/`.

## What runs standalone

| Status | Count | Meaning |
|---|---|---|
| ok | 160 | Runs clean on its own. |
| needs earlier listing | 43 | Continues an earlier listing; needs names defined there. |
| needs input | 8 | Calls `input()`, so it waits for the user. |
| raises by design | 4 | Deliberately raises, to demonstrate an error. |
| teaching failure | 1 | Fails on purpose to show a scope error. |
| needs a data file | 2 | See the notes in the index below. |

## Checked against the book

Of the scripts that run on their own and have printed output in the book,
all but two reproduce that output exactly. The two exceptions are a module
that only defines a function (Chapter 5), and the Chapter 13 stability demo,
which prints all three systems where the book shows each one separately.

The five listings that printed something different from the book in J1
(Chapters 8, 10, 12, 13 and 14) are all corrected in the J2 book, and these
scripts follow J2.

Tested with Python 3.10, NumPy 2.2, SciPy 1.15, pandas 2.3, Matplotlib 3.10
and scikit-learn 1.7. Chapter 13 needs NumPy 2.0 or later for
`np.trapezoid()`.

## Data files

| File | Used by |
|---|---|
| `bench_rc.csv` | Ch 7, 12, 14 --- the recurring bench dataset (Appendix C) |
| `tempData.xlsx`, `tempData.csv` | Ch 10 --- temperature conversion |
| `circuit_analysis.xlsx` | Ch 10 --- ten mesh-circuit configurations |
| `dac_signal.csv` | Ch 12 --- DAC interpolation comparison |
| `reduced_ecg_signal.csv` | Ch 12 --- ECG spline interpolation |
| `sensor_calibration.xlsx` | Ch 12 --- sensor calibration fit |
| `internetusage.xlsx` | Ch 12 --- internet-usage polynomial fit |
| `waterusage.xlsx` | Ch 12 --- water-usage R² comparison |

The Chapter 14 files `dataTemp1.csv`, `daypersample.txt` and `employees.csv`
are not yet included.

Reading the `.xlsx` files needs `openpyxl` (`pip install openpyxl`).

## Index

### `appendixA/`

| Script | Book output? | Status |
|---|---|---|
| `01_using_a_for_loop_for_printing.py` | yes |  |
| `02_fun_to_try_a_degree_to_radian_table.py` | -- | needs input |

### `appendixB/`

| Script | Book output? | Status |
|---|---|---|
| `01_the_legacy_np_matrix_type_key_differences_at.py` | yes |  |

### `chapter02/` --- Your First Python Programs

| Script | Book output? | Status |
|---|---|---|
| `01_translating_math_notation_to_code_math_sqrt.py` | -- |  |
| `02_translating_math_notation_to_code_listing.py` | -- |  |
| `03_reading_the_values_from_the_console.py` | yes | needs input |

### `chapter03/` --- Numbers, Variables and Units

| Script | Book output? | Status |
|---|---|---|
| `01_basic_operations_with_complex_numbers.py` | -- |  |
| `02_creating_strings.py` | -- |  |
| `03_string_methods.py` | -- |  |
| `04_adding_elements_to_a_list.py` | -- |  |
| `05_removing_elements_from_a_list.py` | -- |  |
| `06_sorting_a_list.py` | -- |  |
| `07_other_useful_list_methods.py` | -- |  |
| `08_testing_immutability_in_python_listing.py` | -- |  |
| `09_testing_immutability_in_python_2.py` | -- |  |
| `10_scientific_notation_in_python.py` | -- |  |
| `11_working_consistently_in_base_units.py` | yes |  |
| `12_naming_conventions.py` | -- |  |

### `chapter04/` --- Decisions and Repetition

| Script | Book output? | Status |
|---|---|---|
| `01_logical_operators_vs_bitwise_operators_and_v.py` | -- |  |
| `02_example_relational_operators.py` | yes |  |
| `03_example_operator_precedence_in_practice.py` | yes |  |
| `04_boolean_operator_drill.py` | -- | needs earlier listing |
| `05_the_if_elif_else_statement_listing.py` | -- | needs earlier listing |
| `06_the_if_elif_else_statement_2.py` | yes |  |
| `07_multiple_conditions_with_if_else.py` | yes | needs input |
| `08_multiple_conditions_with_if_elif_else.py` | yes | needs input |
| `09_nested_if.py` | yes | needs input |
| `10_compound_interest_calculation_using_a_for_lo.py` | yes |  |
| `11_loops_as_summation_operators_sigma.py` | -- |  |
| `12_compound_interest_calculation_using_a_while.py` | yes |  |
| `13_a_using_append.py` | yes |  |
| `14_b_using.py` | yes |  |
| `15_compound_interest_with_nested_loops_for_mult.py` | yes |  |
| `16_the_continue_statement.py` | yes |  |
| `17_random_number_guessing_game_using_a_while_lo.py` | yes | needs input |

### `chapter05/` --- Functions and Reusable Calculations

| Script | Book output? | Status |
|---|---|---|
| `01_built_in_functions.py` | yes |  |
| `02_library_functions.py` | -- |  |
| `03_standard_function_single_input_multiple_outp.py` | -- |  |
| `04_standard_function_multiple_input_multiple_ou.py` | -- |  |
| `05_local_functions.py` | -- |  |
| `06_multiple_local_functions.py` | -- |  |
| `07_adding_help_documentation_to_functions.py` | -- |  |
| `08_selective_output_handling_motion.py` | -- |  |
| `09_selective_output_handling_listing.py` | -- | needs earlier listing |
| `10_creating_and_using_a_module_add.py` | -- |  |
| `11_creating_and_using_a_module_math_operations_add.py` | -- |  |
| `12_creating_and_using_a_module_listing.py` | -- |  |
| `13_structure_of_a_python_program.py` | -- |  |
| `14_simple_example_greeting_function.py` | -- |  |
| `15_practical_example_temperature_conversion.py` | -- |  |
| `16_case_1_a_local_variable_shadows_the_global_v.py` | yes |  |
| `17_scope_errors_can_be_masked.py` | -- | raises by design |
| `18_without_the_global_keyword_an_error.py` | yes | teaching failure |
| `19_with_the_global_keyword_correct_modification.py` | yes |  |
| `20_example_nested_functions_in_the_main_program.py` | yes |  |
| `21_example_nested_functions_inside_a_module.py` | yes | module only; the printed output appears when `module_top()` is called |
| `22_nested_enclosing_scope_a_simple_recap.py` | -- |  |
| `23_simple_function_test.py` | -- |  |
| `24_worked_example_legoland_discount.py` | -- | raises by design |
| `25_programming_questions_is_palindrome.py` | -- |  |
| `26_programming_questions_average.py` | -- |  |

### `chapter06/` --- Arrays and Vectorised Computation

| Script | Book output? | Status |
|---|---|---|
| `01_creating_and_printing_vectors_in_numpy.py` | yes |  |
| `02_subscripting_notation_in_numpy.py` | -- |  |
| `03_selecting_rows_columns_subarrays_and_element.py` | yes |  |
| `04_slicing_specific_rows_from_a_2d_array.py` | yes |  |
| `05_using_linspace_and_arange.py` | yes |  |
| `06_selecting_columns_rows_and_subarrays.py` | yes |  |
| `07_selecting_elements_from_specific_dimensions.py` | yes |  |
| `08_selecting_a_range_of_rows_and_flattening_a_2.py` | yes |  |
| `09_array_splitting_practice.py` | -- | needs earlier listing |
| `10_element_wise_addition_subtraction_multiplica_np_array.py` | yes |  |
| `11_element_wise_addition_subtraction_multiplica_listing.py` | yes | needs earlier listing |
| `12_element_wise_addition_subtraction_multiplica_3.py` | yes | needs earlier listing |
| `13_element_wise_addition_subtraction_multiplica_4.py` | yes | needs earlier listing |
| `14_array_attributes_np_array.py` | yes |  |
| `15_array_attributes_listing.py` | yes | needs earlier listing |
| `16_compound_interest.py` | yes |  |
| `17_vertical_displacement.py` | yes |  |
| `18_volume_of_cones.py` | yes |  |
| `19_ee_focus_holding_the_bench_recording_in_arra.py` | yes |  |
| `20_selecting_values_with_a_boolean_mask.py` | -- |  |
| `21_example_logical_operators_with_numpy.py` | yes |  |

### `chapter07/` --- Data Visualisation

| Script | Book output? | Status |
|---|---|---|
| `01_2_d_line_plot_example.py` | -- |  |
| `02_basic_line_and_marker_styles.py` | -- |  |
| `03_2_d_plot_with_several_plot_properties.py` | -- |  |
| `04_multiple_plots_on_a_single_graph.py` | -- |  |
| `05_subplot_upper_and_lower_plot.py` | -- |  |
| `06_subplot_rc_circuit_example.py` | -- |  |
| `07_subplot_quadrant.py` | -- |  |
| `08_stem_plot_discrete_signals.py` | -- |  |
| `09_logarithmic_plots.py` | -- |  |
| `10_an_engineering_application_the_bode_plot.py` | yes |  |
| `11_histogram.py` | -- |  |
| `12_basic_box_plot.py` | -- |  |
| `13_notched_box_plot.py` | -- |  |
| `14_grouped_box_plot.py` | -- |  |
| `15_horizontal_box_plot.py` | -- |  |
| `16_scatter_box_plot.py` | -- |  |
| `17_plotting_the_bench_experiment.py` | -- |  |
| `18_preview_what_is_a_slope.py` | yes |  |

### `chapter08/` --- Complex Numbers as an Engineering Tool

| Script | Book output? | Status |
|---|---|---|
| `01_complex_numbers_in_python_listing.py` | -- |  |
| `02_complex_numbers_in_python_np_abs.py` | -- |  |
| `03_complex_numbers_in_python_np_degrees.py` | yes |  |
| `04_a_simple_series_circuit.py` | yes |  |
| `05_complex_numbers_as_vectors.py` | -- |  |
| `06_a_complete_engineering_example.py` | yes |  |

### `chapter09/` --- Matrices and Circuit Equations

| Script | Book output? | Status |
|---|---|---|
| `01_solving_it_in_python.py` | yes |  |
| `02_what_solving_a_matrix_equation_means.py` | -- | raises by design |
| `03_matrix_addition_subtraction_multiplication_d_np_array.py` | yes |  |
| `04_matrix_addition_subtraction_multiplication_d_listing.py` | yes | needs earlier listing |
| `05_matrix_addition_subtraction_multiplication_d_np_matmul.py` | yes | needs earlier listing |
| `06_matrix_addition_subtraction_multiplication_d_np_linalg.py` | yes | needs earlier listing |
| `07_matrix_addition_subtraction_multiplication_d_5.py` | yes | needs earlier listing |
| `08_precedence_of_matrix_operations_np_array.py` | yes |  |
| `09_precedence_of_matrix_operations_listing.py` | yes | needs earlier listing |
| `10_precedence_of_matrix_operations_np_linalg.py` | yes | needs earlier listing |
| `11_precedence_of_matrix_operations_4.py` | yes | needs earlier listing |
| `12_conjugate_transpose_vs_pure_transpose.py` | yes |  |
| `13_arithmetic_operator_drill.py` | -- | needs earlier listing |

### `chapter10/` --- Measurements, Files and Spreadsheets

| Script | Book output? | Status |
|---|---|---|
| `01_example_requesting_user_input.py` | yes | needs input |
| `02_example_basic_text_file_handling_with_open_r.py` | -- |  |
| `03_example_using_pickle_for_serialising_and_des.py` | -- |  |
| `04_example_using_numpy_save_and_numpy_load_for.py` | -- |  |
| `05_example_binary_file_handling_with_open_in_bi.py` | -- |  |
| `06_example_greek_letter_conversion_table_greek_to_hex.py` | -- |  |
| `07_example_greek_letter_conversion_table_listing.py` | -- |  |
| `08_reading_and_writing_spreadsheets.py` | -- | needs earlier listing |
| `09_example_temperature_data_celsius_to_fahrenhe.py` | yes |  |
| `10_the_separate_ir_r_function.py` | -- |  |
| `11_the_mesh_solver_v_r_function.py` | -- |  |
| `12_reading_the_spreadsheet_and_setting_up.py` | -- |  |
| `13_computing_the_currents.py` | -- | needs earlier listing |
| `14_writing_the_results_back_to_excel.py` | -- | needs earlier listing |
| `15_example_csv_for_temperature_data.py` | -- |  |

### `chapter11/` --- Handling Imperfect Engineering Data

| Script | Book output? | Status |
|---|---|---|
| `01_the_try_except_anatomy.py` | -- | raises by design |
| `02_handling_user_input_safely.py` | -- | needs input |
| `03_using_finally_for_cleanup.py` | -- |  |
| `04_ee_focus_patching_a_sensor_dropout.py` | yes |  |
| `05_handling_missing_data_and_interpolation_np_arange.py` | -- |  |
| `06_handling_missing_data_and_interpolation_plt_subplots.py` | -- | needs earlier listing |
| `07_investigating_a_suspicious_reading_np_arange.py` | -- |  |
| `08_investigating_a_suspicious_reading_np_zeros.py` | -- | needs earlier listing |
| `09_data_imputation.py` | yes |  |

### `chapter12/` --- Interpolation, Curve Fitting and Calibration

| Script | Book output? | Status |
|---|---|---|
| `01_comparing_interpolation_methods.py` | -- |  |
| `02_air_pollutant_index_api_calculation_during_a.py` | -- |  |
| `03_enhancing_ecg_signal_accuracy_with_spline_in.py` | -- |  |
| `04_comparison_of_interpolation_methods_for_sign_pd_read_csv.py` | -- |  |
| `05_comparison_of_interpolation_methods_for_sign_plt_subplot.py` | -- | needs earlier listing |
| `06_straight_line_trendlines.py` | yes |  |
| `07_sensor_calibration_using_polynomial_curve_fi_pd_read_excel.py` | -- |  |
| `08_sensor_calibration_using_polynomial_curve_fi_plt_scatter.py` | yes | needs earlier listing |
| `09_predicting_internet_usage_with_polynomial_cu_pd_read_excel.py` | -- |  |
| `10_predicting_internet_usage_with_polynomial_cu_np_polyval.py` | -- | needs earlier listing |
| `11_predicting_internet_usage_with_polynomial_cu_plt_plot.py` | -- | needs earlier listing |
| `12_predicting_internet_usage_with_polynomial_cu_plt_title.py` | yes | needs earlier listing |
| `13_polynomial_curve_fitting_with_r_squared_eval_pd_read_excel.py` | -- |  |
| `14_polynomial_curve_fitting_with_r_squared_eval_np_sum.py` | yes | needs earlier listing |
| `15_polynomial_curve_fitting_with_r_squared_eval_plt_xlabel.py` | yes | needs earlier listing |
| `16_ee_focus_measuring_the_time_constant_of_the.py` | yes |  |

### `chapter13/` --- Numerical Calculus and System Models

| Script | Book output? | Status |
|---|---|---|
| `01_visualising_the_derivative_limit.py` | yes |  |
| `02_application_finding_capacitor_current_from_a.py` | -- |  |
| `03_ee_focus_checking_the_bench_recording_agains.py` | yes |  |
| `04_application_finding_capacitor_charge_from_a_np_linspace.py` | -- |  |
| `05_application_finding_capacitor_charge_from_a_listing.py` | yes |  |
| `06_bridge_slopes_and_sums_in_the_lab_an_intuiti.py` | yes |  |
| `07_polynomial_multiplication.py` | yes |  |
| `08_polynomial_division.py` | yes |  |
| `09_combined_example_multiplication_and_division.py` | yes |  |
| `10_polynomial_representation_for_motor_control.py` | yes |  |
| `11_polynomial_evaluation.py` | yes |  |
| `12_polynomial_evaluation_for_frequency_response_np_logspace.py` | -- |  |
| `13_polynomial_evaluation_for_frequency_response_plt_figure.py` | -- | needs earlier listing |
| `14_polynomial_roots.py` | yes |  |
| `15_analysing_vertical_motion_np_roots.py` | -- |  |
| `16_analysing_vertical_motion_np_arange.py` | -- | needs earlier listing |
| `17_stability_analysis_of_a_pid_control_system_u_np_convolve.py` | -- |  |
| `18_stability_analysis_of_a_pid_control_system_u_listing.py` | yes | prints all three systems; the book shows each one separately |

### `chapter14/` --- Engineering Statistics and Data Analysis

| Script | Book output? | Status |
|---|---|---|
| `01_population_and_sample.py` | yes |  |
| `02_mean_range_variance_and_standard_deviation.py` | yes |  |
| `03_measurement_error.py` | yes | needs earlier listing |
| `04_applying_this_to_the_bench_dataset.py` | yes |  |
| `05_calculating_mean_along_rows_and_columns_usin.py` | yes |  |
| `06_calculating_the_mean_of_the_entire_matrix_us.py` | yes |  |
| `07_temperature_data_analysis_with_python_np_zeros.py` | -- |  |
| `08_temperature_data_analysis_with_python_plt_plot.py` | -- |  |
| `09_temperature_data_analysis_with_python_pd_read_csv.py` | yes | needs a data file; needs `dataTemp1.csv` and `daypersample.txt` (not yet in the repository) |
| `10_numpy_sorting_examples_np_array.py` | yes |  |
| `11_numpy_sorting_examples_np_sort.py` | yes | needs earlier listing |
| `12_numpy_sorting_examples_listing.py` | yes | needs earlier listing |
| `13_finding_the_top_2_highest_and_lowest_tempera_np_array.py` | -- |  |
| `14_finding_the_top_2_highest_and_lowest_tempera_listing.py` | yes | needs earlier listing |
| `15_creating_a_dataframe.py` | yes |  |
| `16_data_aggregation_with_groupby.py` | yes |  |
| `17_testing_df_isnull_with_a_pandas_dataframe.py` | yes |  |
| `18_using_boxplots.py` | -- |  |
| `19_detecting_outliers_pd_dataframe.py` | yes |  |
| `20_detecting_outliers_df_drop.py` | yes | needs earlier listing |
| `21_descriptive_analytics_bivariate.py` | -- |  |
| `22_predictive_analytics.py` | yes |  |
| `23_prescriptive_analytics.py` | -- |  |
| `24_visualising_an_analysis.py` | -- |  |

### `chapter15/` --- A First Look at Machine Learning

| Script | Book output? | Status |
|---|---|---|
| `01_preparing_data_cleaning_and_scaling.py` | -- |  |
| `02_classification_with_a_decision_tree.py` | yes |  |
| `03_regression_predicting_a_quantity.py` | yes |  |
| `04_training_and_testing_sets.py` | yes |  |

### `chapter16/` --- A First Look at Object-Oriented Python

| Script | Book output? | Status |
|---|---|---|
| `01_defining_a_class.py` | yes |  |
| `02_adding_methods.py` | yes |  |
| `03_inheritance_sharing_behaviour_component.py` | -- |  |
| `04_inheritance_sharing_behaviour_np_degrees.py` | yes | needs earlier listing |
| `05_ee_focus_wrapping_the_bench_recording_signal.py` | -- |  |
| `06_ee_focus_wrapping_the_bench_recording_np_arange.py` | yes | needs earlier listing |

### `cheatsheet/`

| Script | Book output? | Status |
|---|---|---|
| `01_listing_f.py` | -- | needs earlier listing |
| `02_listing_s_strip.py` | -- | needs earlier listing |
| `03_listing_np_array.py` | -- | needs earlier listing |
| `04_listing_np_diff.py` | -- | needs earlier listing |
| `05_listing_np_angle.py` | -- | needs earlier listing |
| `06_listing_plt_plot.py` | -- | needs earlier listing |
| `07_listing_pd_read_csv.py` | -- | needs a data file; `d.csv` is a placeholder name |
