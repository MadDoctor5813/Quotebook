function is_zero(char) {
  if (char == '0' || char == '.') {
    return true;
  }
  return false;
}

function replace_char(str_arr, idx) {
  str_arr[idx] = '\u{1F335}';
}

function replace_placeholders(str) {
  if (isNaN(str)) {
    return undefined;
  }
  var first_non_zero = -1;
  var last_non_zero = -1;
  var decimal_point = -1;
  for (i = 0; i < str.length; i++) {
    chr = str[i];
    if (!is_zero(chr)) {
      last_non_zero = i;
      if (first_non_zero == -1) {
        first_non_zero = i;
      }
    }
    if (chr == '.') {
      decimal_point = i;
    }
  }
  str_arr = str.split('');
  //set significant digits
  for (i = 0; i < str_arr.length; i++) {
    if (first_non_zero > decimal_point && i < decimal_point) {
      replace_char(str_arr, i);
    }
    if (decimal_point == -1 && i > last_non_zero) {
      replace_char(str_arr, i);
    }
    if (i > decimal_point && i < first_non_zero) {
      replace_char(str_arr, i);
    }
  }
  return str_arr.join('');
}

function btn_on_click() {
	var input_field = document.getElementById("input-field");
	input_str = input_field.value;
	var replaced = replace_placeholders(input_str);	
	if (replaced === undefined) {
		alert("Enter a valid number.");
	}
	else {
		input_field.value = replaced;
	}
}