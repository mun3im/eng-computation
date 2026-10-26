# Code listings from *Engineering Computation with Python*

Every code listing longer than five lines, extracted from the book's LaTeX
source into runnable `.py` files. Generated from edition **J1a**.

**215 scripts** in 17 folders, named `NN_description.py`,
where `NN` is the order of appearance in the chapter.

Each file's docstring names the chapter and section it came from, the exact
source file and line, and -- where the book prints one -- the output the book
says the code produces. That makes every script checkable against the book.

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

## What runs standalone

| Status | Count | Meaning |
|---|---|---|
| ok | 145 | Runs clean on its own. |
| needs earlier listing | 51 | Continues an earlier listing; needs names or a module defined there. |
| needs input | 8 | Calls `input()`, so it waits for the user. |
| needs a data file | 7 | Reads a data file the book does not ship -- see below. |
| raises by design | 2 | Deliberately raises, to demonstrate an error or a bug. |
| teaching failure | 2 | Fails on purpose: an `UnboundLocalError` demo, and a syntax skeleton. |

## Known issues in the book's code

These scripts reproduce the book's listings **verbatim**, so four of them print
something different from what the printed page shows. The code is left as the
book has it, so the scripts stay a faithful reference; the fixes are below.

| Script | What happens | Fix |
|---|---|---|
| `chapter08/04_a_simple_series_circuit.py` | prints `Inductor Impedance:  0.00+75.40jj Ohms`, not `75.40j Ohms` — `Z_L` is complex, so `{Z_L:.2f}` renders both parts and the literal `j` is appended to that | use `{Z_L.imag:.2f}j` |
| `chapter13/01_visualizing_the_derivative_limit.py` | three of five table rows differ from the book in the last digit (`h` = 0.01, 0.001, 0.0001) | the script's output is correct; the book's table needs updating |
| `chapter12/06_straight_line_trendlines.py` | prints `Fitted values:` at full precision, not the two decimals shown | `print("Fitted values:", np.round(y_fit, 2))` |
| `chapter14/26_simple_decision_tree_classifier.py` | prints `['high']` — `predict()` returns an array, one answer per input row — not `'high'` | index it: `model.predict([[3]])[0]` |

In every case the underlying numbers are right; only the formatting, or the
output as transcribed into the book, is wrong.

## Data files

`bench_rc.csv` (Appendix C) is copied into the chapter folders that read it,
so those listings run as-is.

Five data files are named by the book but are **not distributed with it**:
`dac_signal.csv`, `reduced_ecg_signal.csv`, `sensor_calibration.xlsx`,
`internetusage.xlsx` and `waterusage.xlsx`. The listings that read them cannot
run until the files are published -- see the Errata chapter of the instructor's
manual, which records this.

## Index

### `appendixA/`

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_using_a_for.py` | appendices/appendixA.tex:380 | -- |  |
| `02_fun_to_try_a_degree_to_radian_table.py` | appendices/appendixA.tex:415 | -- | needs input |

### `appendixB/`

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_detailed_comparison_of_np_array.py` | appendices/appendixB.tex:63 | yes |  |

### `chapter02/` --- Your First Python Programs

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_translating_math_notation_to_code_math_sqrt.py` | chapters/chapter2.tex:148 | -- |  |
| `02_translating_math_notation_to_code_listing.py` | chapters/chapter2.tex:169 | -- |  |
| `03_reading_the_values_from_the_console.py` | chapters/chapter2.tex:381 | -- | needs input |

### `chapter03/` --- Numbers, Variables and Units

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_basic_operations_with_complex_numbers.py` | chapters/chapter3.tex:62 | -- |  |
| `02_creating_strings.py` | chapters/chapter3.tex:113 | -- |  |
| `03_string_methods.py` | chapters/chapter3.tex:155 | -- |  |
| `04_adding_elements_to_a_list.py` | chapters/chapter3.tex:263 | -- |  |
| `05_removing_elements_from_a_list.py` | chapters/chapter3.tex:282 | -- |  |
| `06_sorting_a_list.py` | chapters/chapter3.tex:302 | -- |  |
| `07_other_useful_list_methods.py` | chapters/chapter3.tex:317 | -- |  |
| `08_testing_immutability_in_python_listing.py` | chapters/chapter3.tex:447 | -- |  |
| `09_testing_immutability_in_python_readings_append.py` | chapters/chapter3.tex:463 | -- |  |
| `10_scientific_notation_in_python.py` | chapters/chapter3.tex:555 | -- |  |
| `11_working_consistently_in_base_units.py` | chapters/chapter3.tex:578 | yes |  |
| `12_naming_conventions.py` | chapters/chapter3.tex:619 | -- |  |

### `chapter04/` --- Decisions and Repetition

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_logical_operators_vs_bitwise_operators_and.py` | chapters/chapter4.tex:131 | -- |  |
| `02_example_relational_operators.py` | chapters/chapter4.tex:145 | -- |  |
| `03_example_operator_precedence_in_practice.py` | chapters/chapter4.tex:232 | -- |  |
| `04_boolean_operator_drill.py` | chapters/chapter4.tex:631 | -- | needs earlier listing |
| `05_the_if_elif_else_statement_listing.py` | chapters/chapter4.tex:713 | -- | needs earlier listing |
| `06_the_if_elif_else_statement_2.py` | chapters/chapter4.tex:726 | -- |  |
| `07_multiple_conditions_with_if_else.py` | chapters/chapter4.tex:772 | -- | needs input |
| `08_multiple_conditions_with_if_elif_else.py` | chapters/chapter4.tex:808 | yes | needs input |
| `09_nested_if.py` | chapters/chapter4.tex:841 | -- | needs input |
| `10_compound_interest_calculation_using_a_for_lo.py` | chapters/chapter4.tex:925 | yes |  |
| `11_loops_as_summation_operators.py` | chapters/chapter4.tex:952 | -- |  |
| `12_compound_interest_calculation_using_a_while.py` | chapters/chapter4.tex:1000 | yes |  |
| `13_a_using_append.py` | chapters/chapter4.tex:1037 | yes |  |
| `14_b_using.py` | chapters/chapter4.tex:1061 | yes |  |
| `15_compound_interest_with_nested_loops_for_mult.py` | chapters/chapter4.tex:1089 | yes |  |
| `16_the_continue_statement.py` | chapters/chapter4.tex:1130 | yes |  |
| `17_random_number_guessing_game_using_a_while_lo.py` | chapters/chapter4.tex:1158 | yes | needs input |

### `chapter05/` --- Functions and Reusable Calculations

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_built_in_functions.py` | chapters/chapter5.tex:171 | yes |  |
| `02_library_functions.py` | chapters/chapter5.tex:204 | -- |  |
| `03_standard_function_single_input_multiple_outp.py` | chapters/chapter5.tex:284 | -- |  |
| `04_standard_function_multiple_input_multiple_ou.py` | chapters/chapter5.tex:310 | -- |  |
| `05_local_functions.py` | chapters/chapter5.tex:328 | -- |  |
| `06_multiple_local_functions.py` | chapters/chapter5.tex:351 | -- |  |
| `07_adding_help_documentation_to_functions.py` | chapters/chapter5.tex:404 | -- |  |
| `08_selective_output_handling_motion.py` | chapters/chapter5.tex:425 | -- |  |
| `09_selective_output_handling_listing.py` | chapters/chapter5.tex:446 | -- | needs earlier listing |
| `10_creating_and_using_a_module_add.py` | chapters/chapter5.tex:481 | -- |  |
| `11_creating_and_using_a_module_math_operations_add.py` | chapters/chapter5.tex:495 | -- | needs earlier listing |
| `12_creating_and_using_a_module_listing.py` | chapters/chapter5.tex:510 | -- | needs earlier listing |
| `13_structure_of_a_python_program.py` | chapters/chapter5.tex:538 | -- |  |
| `14_simple_example_greeting_function.py` | chapters/chapter5.tex:563 | -- |  |
| `15_practical_example_temperature_conversion.py` | chapters/chapter5.tex:582 | -- |  |
| `16_case_1_a_local_variable_shadows_the_global_v.py` | chapters/chapter5.tex:717 | -- |  |
| `17_scope_errors_can_be_masked.py` | chapters/chapter5.tex:767 | -- | needs earlier listing |
| `18_without_the_global.py` | chapters/chapter5.tex:796 | -- | teaching failure |
| `19_with_the_global.py` | chapters/chapter5.tex:819 | -- |  |
| `20_example_nested_functions_in_the_main_program.py` | chapters/chapter5.tex:892 | -- |  |
| `21_example_nested_functions_inside_a_module.py` | chapters/chapter5.tex:930 | -- |  |
| `22_nested_enclosing_scope_a_simple_recap.py` | chapters/chapter5.tex:976 | -- |  |
| `23_simple_function_test.py` | chapters/chapter5.tex:1090 | -- |  |
| `24_worked_example_legoland_discount.py` | chapters/chapter5.tex:1126 | -- | raises by design |
| `25_programming_questions_is_palindrome.py` | chapters/chapter5.tex:1205 | -- |  |
| `26_programming_questions_average.py` | chapters/chapter5.tex:1216 | -- |  |

### `chapter06/` --- Arrays and Vectorized Computation

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_creating_and_printing_vectors_in_numpy.py` | chapters/chapter6.tex:218 | yes |  |
| `02_subscripting_notation_in_numpy.py` | chapters/chapter6.tex:276 | -- |  |
| `03_selecting_rows_columns_subarrays_and_element.py` | chapters/chapter6.tex:297 | yes |  |
| `04_slicing_specific_rows_from_a_2d_array.py` | chapters/chapter6.tex:377 | yes |  |
| `05_using_linspace.py` | chapters/chapter6.tex:438 | yes |  |
| `06_selecting_columns_rows_and_subarrays.py` | chapters/chapter6.tex:492 | yes |  |
| `07_selecting_elements_from_specific_dimensions.py` | chapters/chapter6.tex:552 | yes |  |
| `08_selecting_a_range_of_rows_and_flattening_a_2.py` | chapters/chapter6.tex:596 | yes |  |
| `09_array_splitting_practice.py` | chapters/chapter6.tex:653 | -- | needs earlier listing |
| `10_element_wise_addition_subtraction_multiplica_np_array.py` | chapters/chapter6.tex:675 | yes |  |
| `11_element_wise_addition_subtraction_multiplica_listing.py` | chapters/chapter6.tex:698 | yes | needs earlier listing |
| `12_element_wise_addition_subtraction_multiplica_3.py` | chapters/chapter6.tex:719 | yes | needs earlier listing |
| `13_element_wise_addition_subtraction_multiplica_4.py` | chapters/chapter6.tex:740 | yes | needs earlier listing |
| `14_array_attributes_np_array.py` | chapters/chapter6.tex:765 | yes |  |
| `15_array_attributes_listing.py` | chapters/chapter6.tex:787 | yes | needs earlier listing |
| `16_compound_interest.py` | chapters/chapter6.tex:910 | yes |  |
| `17_vertical_displacement.py` | chapters/chapter6.tex:947 | yes |  |
| `18_volume_of_cones_np_array.py` | chapters/chapter6.tex:974 | yes |  |
| `19_volume_of_cones_np_arange.py` | chapters/chapter6.tex:1000 | yes |  |
| `20_example_logical_operators_with_numpy.py` | chapters/chapter6.tex:1065 | -- |  |

### `chapter07/` --- Data Visualization

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_2_d_line_plot_example.py` | chapters/chapter7.tex:91 | -- |  |
| `02_basic_line_and_marker_styles.py` | chapters/chapter7.tex:183 | -- |  |
| `03_2_d_plot_with_several_plot_properties.py` | chapters/chapter7.tex:251 | -- |  |
| `04_multiple_plots_on_a_single_graph.py` | chapters/chapter7.tex:286 | -- |  |
| `05_subplot_upper_and_lower_plot.py` | chapters/chapter7.tex:331 | -- |  |
| `06_subplot_rc_circuit_example.py` | chapters/chapter7.tex:394 | -- |  |
| `07_subplot_quadrant.py` | chapters/chapter7.tex:449 | -- |  |
| `08_stem_plot_discrete_signals.py` | chapters/chapter7.tex:481 | -- |  |
| `09_logarithmic_plots.py` | chapters/chapter7.tex:543 | -- |  |
| `10_bode_plot_of_an_rc_low_pass_filter.py` | chapters/chapter7.tex:596 | yes |  |
| `11_histogram.py` | chapters/chapter7.tex:660 | -- |  |
| `12_basic_box_plot.py` | chapters/chapter7.tex:685 | -- |  |
| `13_notched_box_plot.py` | chapters/chapter7.tex:709 | -- |  |
| `14_grouped_box_plot.py` | chapters/chapter7.tex:733 | -- |  |
| `15_horizontal_box_plot.py` | chapters/chapter7.tex:760 | -- |  |
| `16_scatter_box_plot.py` | chapters/chapter7.tex:784 | -- |  |
| `17_plotting_the_bench_experiment.py` | chapters/chapter7.tex:823 | -- |  |
| `18_preview_what_is_a_slope.py` | chapters/chapter7.tex:868 | yes |  |

### `chapter08/` --- Complex Numbers as an Engineering Tool

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_complex_numbers_in_python_listing.py` | chapters/chapter8.tex:85 | -- |  |
| `02_complex_numbers_in_python_np_abs.py` | chapters/chapter8.tex:97 | -- |  |
| `03_complex_numbers_in_python_np_radians.py` | chapters/chapter8.tex:115 | yes |  |
| `04_a_simple_series_circuit.py` | chapters/chapter8.tex:169 | yes |  |
| `05_a_complete_engineering_example.py` | chapters/chapter8.tex:240 | yes |  |

### `chapter09/` --- Matrices and Circuit Equations

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_why_circuits_need_matrices.py` | chapters/chapter9.tex:51 | yes |  |
| `02_what_solving_a_matrix_equation_means.py` | chapters/chapter9.tex:126 | -- | raises by design |
| `03_matrix_addition_subtraction_multiplication_d_np_array.py` | chapters/chapter9.tex:319 | yes |  |
| `04_matrix_addition_subtraction_multiplication_d_listing.py` | chapters/chapter9.tex:342 | yes | needs earlier listing |
| `05_matrix_addition_subtraction_multiplication_d_np_matmul.py` | chapters/chapter9.tex:363 | yes | needs earlier listing |
| `06_matrix_addition_subtraction_multiplication_d_linalg_solve.py` | chapters/chapter9.tex:385 | yes | needs earlier listing |
| `07_matrix_addition_subtraction_multiplication_d_linalg_matrix_power.py` | chapters/chapter9.tex:408 | yes | needs earlier listing |
| `08_precedence_of_matrix_operations_np_array.py` | chapters/chapter9.tex:445 | yes |  |
| `09_precedence_of_matrix_operations_listing.py` | chapters/chapter9.tex:468 | yes | needs earlier listing |
| `10_precedence_of_matrix_operations_linalg_matrix_power.py` | chapters/chapter9.tex:491 | yes | needs earlier listing |
| `11_precedence_of_matrix_operations_4.py` | chapters/chapter9.tex:514 | yes | needs earlier listing |
| `12_conjugate_transpose_vs_pure_transpose.py` | chapters/chapter9.tex:543 | yes |  |
| `13_arithmetic_operator_drill.py` | chapters/chapter9.tex:584 | -- | needs earlier listing |

### `chapter10/` --- Measurements, Files and Spreadsheets

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_requesting_prompt_input.py` | chapters/chapter10.tex:97 | -- | needs input |
| `02_text_data.py` | chapters/chapter10.tex:293 | -- |  |
| `03_binary_data_pickle_dump.py` | chapters/chapter10.tex:310 | -- |  |
| `04_binary_data_np_array.py` | chapters/chapter10.tex:328 | -- |  |
| `05_binary_data_file_write.py` | chapters/chapter10.tex:344 | -- |  |
| `06_example_greek_letter_conversion_table_greek_to_hex.py` | chapters/chapter10.tex:368 | -- |  |
| `07_example_greek_letter_conversion_table_listing.py` | chapters/chapter10.tex:390 | -- | needs earlier listing |
| `08_reading_and_writing_spreadsheets.py` | chapters/chapter10.tex:408 | -- | needs earlier listing |
| `09_example_temperature_data_celsius_to_fahrenhe.py` | chapters/chapter10.tex:442 | -- | needs earlier listing |
| `10_the_separate_ir_r.py` | chapters/chapter10.tex:545 | -- |  |
| `11_the_mesh_solver_v_r.py` | chapters/chapter10.tex:580 | -- |  |
| `12_reading_the_spreadsheet_and_setting_up.py` | chapters/chapter10.tex:637 | -- | needs earlier listing |
| `13_computing_the_currents.py` | chapters/chapter10.tex:666 | -- | needs earlier listing |
| `14_writing_the_results_back_to_excel.py` | chapters/chapter10.tex:700 | -- | needs earlier listing |
| `15_example_csv_for_temperature_data.py` | chapters/chapter10.tex:743 | -- | needs a data file |

### `chapter11/` --- Handling Imperfect Engineering Data

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_general_structure_of_try_except_else_finally.py` | chapters/chapter11.tex:51 | -- | teaching failure |
| `02_handling_multiple_possible_exceptions_from_u.py` | chapters/chapter11.tex:430 | -- | needs input |
| `03_try_except_finally_for_safe_file_handling.py` | chapters/chapter11.tex:463 | -- |  |
| `04_repairing_a_signal_by_interpolation.py` | chapters/chapter11.tex:659 | yes |  |
| `05_handling_missing_data_and_interpolation_np_arange.py` | chapters/chapter11.tex:707 | -- |  |
| `06_handling_missing_data_and_interpolation_plt_subplots.py` | chapters/chapter11.tex:727 | -- | needs earlier listing |
| `07_investigating_a_suspicious_reading_np_arange.py` | chapters/chapter11.tex:777 | -- |  |
| `08_investigating_a_suspicious_reading_np_zeros.py` | chapters/chapter11.tex:815 | -- | needs earlier listing |
| `09_data_imputation.py` | chapters/chapter11.tex:847 | yes |  |

### `chapter12/` --- Interpolation, Curve Fitting and Calibration

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_comparing_interpolation_methods.py` | chapters/chapter12.tex:120 | -- |  |
| `02_air_pollutant_index_api_calculation_during_a.py` | chapters/chapter12.tex:230 | -- |  |
| `03_enhancing_ecg_signal_accuracy_with_spline_in.py` | chapters/chapter12.tex:320 | -- | needs a data file |
| `04_comparison_of_interpolation_methods_for_sign_np_linspace.py` | chapters/chapter12.tex:393 | -- | needs a data file |
| `05_comparison_of_interpolation_methods_for_sign_plt_subplot.py` | chapters/chapter12.tex:424 | -- | needs earlier listing |
| `06_straight_line_trendlines.py` | chapters/chapter12.tex:477 | yes |  |
| `07_sensor_calibration_using_polynomial_curve_fi_np_polyfit.py` | chapters/chapter12.tex:536 | -- | needs a data file |
| `08_sensor_calibration_using_polynomial_curve_fi_plt_scatter.py` | chapters/chapter12.tex:559 | -- | needs earlier listing |
| `09_predicting_internet_usage_with_polynomial_cu_np_polyfit.py` | chapters/chapter12.tex:615 | -- | needs a data file |
| `10_predicting_internet_usage_with_polynomial_cu_np_polyval.py` | chapters/chapter12.tex:639 | -- | needs earlier listing |
| `11_predicting_internet_usage_with_polynomial_cu_np_concatenate.py` | chapters/chapter12.tex:657 | -- | needs earlier listing |
| `12_predicting_internet_usage_with_polynomial_cu_plt_title.py` | chapters/chapter12.tex:677 | -- | needs earlier listing |
| `13_polynomial_curve_fitting_with_r_squared_eval_np_polyval.py` | chapters/chapter12.tex:728 | -- | needs a data file |
| `14_polynomial_curve_fitting_with_r_squared_eval_np_sum.py` | chapters/chapter12.tex:747 | -- | needs earlier listing |
| `15_polynomial_curve_fitting_with_r_squared_eval_np_polyfit.py` | chapters/chapter12.tex:770 | -- | needs earlier listing |
| `16_ee_focus_measuring_the_time_constant_of_the.py` | chapters/chapter12.tex:813 | yes |  |

### `chapter13/` --- Numerical Calculus and System Models

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_visualizing_the_derivative_limit.py` | chapters/chapter13.tex:88 | yes |  |
| `02_the_mathematical_gradient_np_linspace.py` | chapters/chapter13.tex:150 | -- |  |
| `03_the_mathematical_gradient_np_arange.py` | chapters/chapter13.tex:215 | yes |  |
| `04_integration_total_accumulation_np_linspace.py` | chapters/chapter13.tex:255 | -- |  |
| `05_integration_total_accumulation_np_trapezoid.py` | chapters/chapter13.tex:303 | yes |  |
| `06_bridge_slopes_and_sums_in_the_lab_an_intuiti.py` | chapters/chapter13.tex:351 | yes |  |
| `07_polynomial_multiplication.py` | chapters/chapter13.tex:464 | -- |  |
| `08_polynomial_division_np_polydiv.py` | chapters/chapter13.tex:486 | -- |  |
| `09_polynomial_division_np_polymul.py` | chapters/chapter13.tex:519 | -- |  |
| `10_polynomial_representation_for_motor_control.py` | chapters/chapter13.tex:592 | -- |  |
| `11_polynomial_evaluation.py` | chapters/chapter13.tex:629 | -- |  |
| `12_polynomial_evaluation_for_frequency_response_np_polyval.py` | chapters/chapter13.tex:654 | -- |  |
| `13_polynomial_evaluation_for_frequency_response_np_abs.py` | chapters/chapter13.tex:678 | -- | needs earlier listing |
| `14_polynomial_roots.py` | chapters/chapter13.tex:705 | -- |  |
| `15_analyzing_vertical_motion_np_roots.py` | chapters/chapter13.tex:749 | -- |  |
| `16_analyzing_vertical_motion_np_arange.py` | chapters/chapter13.tex:768 | -- | needs earlier listing |
| `17_stability_analysis_of_a_pid_control_system_u_check_stability.py` | chapters/chapter13.tex:808 | -- |  |
| `18_stability_analysis_of_a_pid_control_system_u_listing.py` | chapters/chapter13.tex:843 | -- | needs earlier listing |

### `chapter14/` --- Engineering Statistics and Data Analysis

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_population_and_sample.py` | chapters/chapter14.tex:72 | yes |  |
| `02_mean_range_variance_and_standard_deviation.py` | chapters/chapter14.tex:108 | yes |  |
| `03_measurement_error.py` | chapters/chapter14.tex:138 | yes | needs earlier listing |
| `04_applying_this_to_the_bench_dataset.py` | chapters/chapter14.tex:160 | yes |  |
| `05_calculating_mean_along_rows_and_columns_usin.py` | chapters/chapter14.tex:212 | -- |  |
| `06_calculating_the_mean_of_the_entire_matrix_us.py` | chapters/chapter14.tex:242 | -- |  |
| `07_the_datastat.py` | chapters/chapter14.tex:276 | -- |  |
| `08_the_plotdata.py` | chapters/chapter14.tex:343 | -- |  |
| `09_temperature_data_analysis_with_python.py` | chapters/chapter14.tex:371 | -- | needs earlier listing |
| `10_numpy_sorting_examples_np_array.py` | chapters/chapter14.tex:430 | yes |  |
| `11_numpy_sorting_examples_np_sort.py` | chapters/chapter14.tex:452 | yes | needs earlier listing |
| `12_numpy_sorting_examples_3.py` | chapters/chapter14.tex:472 | yes | needs earlier listing |
| `13_finding_the_top_2_highest_and_lowest_tempera_np_sort.py` | chapters/chapter14.tex:504 | -- |  |
| `14_finding_the_top_2_highest_and_lowest_tempera_listing.py` | chapters/chapter14.tex:523 | yes | needs earlier listing |
| `15_creating_a_dataframe.py` | chapters/chapter14.tex:789 | yes |  |
| `16_data_aggregation_with_groupby.py` | chapters/chapter14.tex:832 | yes |  |
| `17_testing_df_isnull.py` | chapters/chapter14.tex:889 | yes |  |
| `18_using_boxplots.py` | chapters/chapter14.tex:1036 | -- |  |
| `19_detecting_outliers_listing.py` | chapters/chapter14.tex:1059 | yes |  |
| `20_detecting_outliers_df_drop.py` | chapters/chapter14.tex:1148 | yes | needs earlier listing |
| `21_descriptive_analytics_bivariate.py` | chapters/chapter14.tex:1240 | -- |  |
| `22_predictive_analytics.py` | chapters/chapter14.tex:1275 | yes |  |
| `23_prescriptive_analytics.py` | chapters/chapter14.tex:1303 | -- |  |
| `24_visualizing_an_analysis.py` | chapters/chapter14.tex:1318 | -- |  |
| `25_data_cleaning_and_scaling_for_machine_learni.py` | chapters/chapter14.tex:1361 | -- |  |
| `26_simple_decision_tree_classifier.py` | chapters/chapter14.tex:1415 | yes |  |
| `27_linear_regression_classifier_example.py` | chapters/chapter14.tex:1446 | yes |  |

### `chapter15/` --- A First Look at Object-Oriented Python

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_defining_a_class.py` | chapters/chapter15.tex:113 | yes |  |
| `02_adding_methods.py` | chapters/chapter15.tex:188 | yes |  |
| `03_inheritance_sharing_behaviour_component.py` | chapters/chapter15.tex:212 | -- |  |
| `04_inheritance_sharing_behaviour_np_degrees.py` | chapters/chapter15.tex:288 | yes | needs earlier listing |
| `05_ee_focus_wrapping_the_bench_recording_signal.py` | chapters/chapter15.tex:319 | -- |  |
| `06_ee_focus_wrapping_the_bench_recording_np_arange.py` | chapters/chapter15.tex:350 | yes | needs earlier listing |

### `cheatsheet/`

| Script | From | Book output? | Status |
|---|---|---|---|
| `01_listing_f.py` | cheatsheet.tex:31 | -- | needs earlier listing |
| `02_listing_s_strip.py` | cheatsheet.tex:57 | -- | needs earlier listing |
| `03_listing_np_array.py` | cheatsheet.tex:93 | -- | needs earlier listing |
| `04_listing_np_diff.py` | cheatsheet.tex:127 | -- | needs earlier listing |
| `05_listing_np_angle.py` | cheatsheet.tex:157 | -- | needs earlier listing |
| `06_listing_plt_plot.py` | cheatsheet.tex:171 | -- | needs earlier listing |
| `07_listing_pd_read_csv.py` | cheatsheet.tex:188 | -- | needs a data file |

