source env/bin/activate
cd tests
CMD="pytest -v"
echo ""
echo -e "\e[34mRunning Tests" #http://misc.flogisoft.com/bash/tip_colors_and_formatting
echo -e "\e[0m"
$CMD ./binary_list_tests.py
$CMD ./identity_tests.py
$CMD ./list_addition_tests.py
$CMD ./spanning_set_tests.py
$CMD ./span_wo_basis_tests.py
$CMD ./binary_conversion_tests.py
$CMD ./get_row_tests.py
$CMD ./generator_matrix_tests.py
$CMD ./get_binary_tests.py
$CMD ./get_parity_tests.py
$CMD ./get_encoding_tests.py
$CMD ./do_parity_tests.py
$CMD ./interleaving_tests.py
$CMD ./calculate_int_tests.py
$CMD ./create_syndrome_tests.py
$CMD ./calculate_syndrome_tests.py
$CMD ./decode_syndrome_tests.py
echo ""
echo -e "\e[34mTESTS COMPLETE"
echo -e "\e[0m"
