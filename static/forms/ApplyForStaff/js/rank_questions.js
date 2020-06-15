$("#id_rank_choices").change(function() {

  // Base Questions
  $('#div1_id_name').hide();
  $('#div_id_name').hide();
  $('#span_id_name').hide();
  $('#span2_id_name').hide();
  $('#div1_id_email').hide();
  $('#div_id_email').hide();
  $('#span_id_email').hide();
  $('#span2_id_email').hide();
  $('#div1_id_ign').hide();
  $('#div_id_ign').hide();
  $('#span_id_ign').hide();
  $('#span2_id_ign').hide();
  $('#div1_id_age').hide();
  $('#div_id_age').hide();
  $('#span_id_age').hide();
  $('#span2_id_age').hide();
  $('#div1_id_timezone').hide();
  $('#div_id_timezone').hide();
  $('#span_id_timezone').hide();
  $('#span2_id_timezone').hide();
  $('#div1_id_time_spend').hide();
  $('#div_id_time_spend').hide();
  $('#span_id_time_spend').hide();
  $('#span2_id_time_spend').hide();
  $('#div1_id_why_staff').hide();
  $('#div_id_why_staff').hide();
  $('#span_id_why_staff').hide();
  $('#span2_id_why_staff').hide();
  $('#div1_id_why_us').hide();
  $('#div_id_why_us').hide();
  $('#span_id_why_us').hide();
  $('#span2_id_why_us').hide();

  // Dev Questions
  $('#div1_id_kind_of_dev').hide();
  $('#div_id_kind_of_dev').hide();
  $('#span_id_kind_of_dev').hide();
  $('#span2_id_kind_of_dev').hide();
  $('#div1_id_dev_creations').hide();
  $('#div_id_dev_creations').hide();
  $('#span_id_dev_creations').hide();
  $('#span2_id_dev_creations').hide();

  $('#id_dev_kind_of_dev').removeAttr('required');
  $('#id_dev_kind_of_dev').data("fullstack");
  $('#id_dev_creations').removeAttr('required');
  $('#id_dev_creations').val("creations");

  // Mod Questions
  $('#div1_id_deal_case').hide();
  $('#div_id_deal_case').hide();
  $('#span_id_deal_case').hide();
  $('#span2_id_deal_case').hide();
  $('#div1_id_mod_previous_experiences').hide();
  $('#div_id_mod_previous_experiences').hide();
  $('#span_id_mod_previous_experiences').hide();
  $('#span2_id_mod_previous_experiences').hide();

  $('#id_mod_how_will_deal_with_a_case').removeAttr('required');
  $('#id_mod_how_will_deal_with_a_case').val("How you will deal with a case:");
  $('#id_mod_previous_experiences').removeAttr('required');
  $('#id_mod_previous_experiences').val("previous experiences");
  // Helper Questions
  $('#div1_id_helper_deal_case').hide();
  $('#div_id_helper_deal_case').hide();
  $('#span_id_helper_deal_case').hide();
  $('#span2_id_helper_deal_case').hide();
  $('#div1_id_helper_previous_experiences').hide();
  $('#div_id_helper_previous_experiences').hide();
  $('#span_id_helper_previous_experiences').hide();
  $('#span2_id_helper_previous_experiences').hide();

  $('#id_helper_how_will_deal_with_a_case').removeAttr('required');
  $('#id_helper_how_will_deal_with_a_case').data("How you will deal with a case:");
  $('#id_helper_previous_experiences').removeAttr('required');
  $('#id_helper_previous_experiences').val("Your previous experiences:");

  // Builder Questions
  $('#div1_id_builder_previous_experiences').hide();
  $('#div_id_builder_previous_experiences').hide();
  $('#span_id_builder_previous_experiences').hide();
  $('#span2_id_builder_previous_experiences').hide();
  $('#div1_id_builder_best_builds').hide();
  $('#div_id_builder_best_builds').hide();
  $('#span_id_builder_best_builds').hide();
  $('#span2_id_builder_best_builds').hide();

  $('#id_builder_previous_build_experiences').removeAttr('required');
  $('#id_builder_previous_build_experiences').val("Previous experiences");
  $('#id_builder_one_of_best_builds').removeAttr('required');
  $('#id_builder_one_of_best_builds').val("Best Builds");

  // Hide button

  $('#div_id_button').hide();
  $('#div2_id_button').hide();
  $('#div3_id_button').hide();
  $('#button_id_button').hide();
  $('#span_id_button').hide();
  $('#i_id_button').hide();

  // Captcha

  $('#div1_id_captcha').hide();
  $('#div_id_captcha').hide();
  $('#span_id_captcha').hide();
  $('#span2_id_captcha').hide();

  if ($(this).val() == "dev") {
    // Base Questions
  $('#div1_id_name').show();
  $('#div_id_name').show();
  $('#span_id_name').show();
  $('#span2_id_name').show();
  $('#div1_id_email').show();
  $('#div_id_email').show();
  $('#span_id_email').show();
  $('#span2_id_email').show();
  $('#div1_id_ign').show();
  $('#div_id_ign').show();
  $('#span_id_ign').show();
  $('#span2_id_ign').show();
  $('#div1_id_age').show();
  $('#div_id_age').show();
  $('#span_id_age').show();
  $('#span2_id_age').show();
  $('#div1_id_timezone').show();
  $('#div_id_timezone').show();
  $('#span_id_timezone').show();
  $('#span2_id_timezone').show();
  $('#div1_id_time_spend').show();
  $('#div_id_time_spend').show();
  $('#span_id_time_spend').show();
  $('#span2_id_time_spend').show();
  $('#div1_id_why_staff').show();
  $('#div_id_why_staff').show();
  $('#span_id_why_staff').show();
  $('#span2_id_why_staff').show();
  $('#div1_id_why_us').show();
  $('#div_id_why_us').show();
  $('#span_id_why_us').show();
  $('#span2_id_why_us').show();


    // Dev Questions
  $('#div1_id_kind_of_dev').show();
  $('#div_id_kind_of_dev').show();
  $('#span_id_kind_of_dev').show();
  $('#span2_id_kind_of_dev').show();
  $('#div1_id_dev_creations').show();
  $('#div_id_dev_creations').show();
  $('#span_id_dev_creations').show();
  $('#span2_id_dev_creations').show();

  // Remove default data
  $('#id_dev_creations').val("");
  $('#id_dev_kind_of_dev').attr('required');
  $('#id_dev_creations').attr('required');

    // Button
    $('#div_id_button').show();
    $('#div2_id_button').show();
    $('#div3_id_button').show();
    $('#button_id_button').show();
    $('#span_id_button').show();
    $('#i_id_button').show();

    // Captcha

  $('#div1_id_captcha').show();
  $('#div_id_captcha').show();
  $('#span_id_captcha').show();
  $('#span2_id_captcha').show();

  }
  if ($(this).val() == "mod") {
    // Base Questions
  $('#div1_id_name').show();
  $('#div_id_name').show();
  $('#span_id_name').show();
  $('#span2_id_name').show();
  $('#div1_id_email').show();
  $('#div_id_email').show();
  $('#span_id_email').show();
  $('#span2_id_email').show();
  $('#div1_id_ign').show();
  $('#div_id_ign').show();
  $('#span_id_ign').show();
  $('#span2_id_ign').show();
  $('#div1_id_age').show();
  $('#div_id_age').show();
  $('#span_id_age').show();
  $('#span2_id_age').show();
  $('#div1_id_timezone').show();
  $('#div_id_timezone').show();
  $('#span_id_timezone').show();
  $('#span2_id_timezone').show();
  $('#div1_id_time_spend').show();
  $('#div_id_time_spend').show();
  $('#span_id_time_spend').show();
  $('#span2_id_time_spend').show();
  $('#div1_id_why_staff').show();
  $('#div_id_why_staff').show();
  $('#span_id_why_staff').show();
  $('#span2_id_why_staff').show();
  $('#div1_id_why_us').show();
  $('#div_id_why_us').show();
  $('#span_id_why_us').show();
  $('#span2_id_why_us').show();


    // Mod Questions
  $('#div1_id_deal_case').show();
  $('#div_id_deal_case').show();
  $('#span_id_deal_case').show();
  $('#span2_id_deal_case').show();
  $('#div1_id_mod_previous_experiences').show();
  $('#div_id_mod_previous_experiences').show();
  $('#span_id_mod_previous_experiences').show();
  $('#span2_id_mod_previous_experiences').show();

  $('#id_mod_how_will_deal_with_a_case').val('');
  $('#id_mod_previous_experiences').val('');
  $('#id_mod_how_will_deal_with_a_case').attr('required');
  $('#id_mod_previous_experiences').attr('required');

    // Button
    $('#div_id_button').show();
    $('#div2_id_button').show();
    $('#div3_id_button').show();
    $('#button_id_button').show();
    $('#span_id_button').show();
    $('#i_id_button').show();

    // Captcha

  $('#div1_id_captcha').show();
  $('#div_id_captcha').show();
  $('#span_id_captcha').show();
  $('#span2_id_captcha').show();

  }
  if ($(this).val() == "builder") {
    // Base Questions
  $('#div1_id_name').show();
  $('#div_id_name').show();
  $('#span_id_name').show();
  $('#span2_id_name').show();
  $('#div1_id_email').show();
  $('#div_id_email').show();
  $('#span_id_email').show();
  $('#span2_id_email').show();
  $('#div1_id_ign').show();
  $('#div_id_ign').show();
  $('#span_id_ign').show();
  $('#span2_id_ign').show();
  $('#div1_id_age').show();
  $('#div_id_age').show();
  $('#span_id_age').show();
  $('#span2_id_age').show();
  $('#div1_id_timezone').show();
  $('#div_id_timezone').show();
  $('#span_id_timezone').show();
  $('#span2_id_timezone').show();
  $('#div1_id_time_spend').show();
  $('#div_id_time_spend').show();
  $('#span_id_time_spend').show();
  $('#span2_id_time_spend').show();
  $('#div1_id_why_staff').show();
  $('#div_id_why_staff').show();
  $('#span_id_why_staff').show();
  $('#span2_id_why_staff').show();
  $('#div1_id_why_us').show();
  $('#div_id_why_us').show();
  $('#span_id_why_us').show();
  $('#span2_id_why_us').show();


    // Builder Questions
  $('#div1_id_builder_previous_experiences').show();
  $('#div_id_builder_previous_experiences').show();
  $('#span_id_builder_previous_experiences').show();
  $('#span2_id_builder_previous_experiences').show();
  $('#div1_id_builder_best_builds').show();
  $('#div_id_builder_best_builds').show();
  $('#span_id_builder_best_builds').show();
  $('#span2_id_builder_best_builds').show();

  $('#id_builder_previous_build_experiences').val("");
  $('#id_builder_one_of_best_builds').val("");
  $('#id_builder_previous_build_experiences').attr('required');
  $('#id_builder_one_of_best_builds').attr('required');


    // Button
    $('#div_id_button').show();
    $('#div2_id_button').show();
    $('#div3_id_button').show();
    $('#button_id_button').show();
    $('#span_id_button').show();
    $('#i_id_button').show();

    // Captcha

  $('#div1_id_captcha').show();
  $('#div_id_captcha').show();
  $('#span_id_captcha').show();
  $('#span2_id_captcha').show();

  }
  if ($(this).val() == "helper") {
    // Base Questions
  $('#div1_id_name').show();
  $('#div_id_name').show();
  $('#span_id_name').show();
  $('#span2_id_name').show();
  $('#div1_id_email').show();
  $('#div_id_email').show();
  $('#span_id_email').show();
  $('#span2_id_email').show();
  $('#div1_id_ign').show();
  $('#div_id_ign').show();
  $('#span_id_ign').show();
  $('#span2_id_ign').show();
  $('#div1_id_age').show();
  $('#div_id_age').show();
  $('#span_id_age').show();
  $('#span2_id_age').show();
  $('#div1_id_timezone').show();
  $('#div_id_timezone').show();
  $('#span_id_timezone').show();
  $('#span2_id_timezone').show();
  $('#div1_id_time_spend').show();
  $('#div_id_time_spend').show();
  $('#span_id_time_spend').show();
  $('#span2_id_time_spend').show();
  $('#div1_id_why_staff').show();
  $('#div_id_why_staff').show();
  $('#span_id_why_staff').show();
  $('#span2_id_why_staff').show();
  $('#div1_id_why_us').show();
  $('#div_id_why_us').show();
  $('#span_id_why_us').show();
  $('#span2_id_why_us').show();


    // Helper Questions
  $('#div1_id_helper_deal_case').show();
  $('#div_id_helper_deal_case').show();
  $('#span_id_helper_deal_case').show();
  $('#span2_id_helper_deal_case').show();
  $('#div1_id_helper_previous_experiences').show();
  $('#div_id_helper_previous_experiences').show();
  $('#span_id_helper_previous_experiences').show();
  $('#span2_id_helper_previous_experiences').show();

  $('#id_helper_how_will_deal_with_a_case').val("");
  $('#id_helper_previous_experiences').val("");
  $('#id_helper_how_will_deal_with_a_case').attr('required');
  $('#id_helper_previous_experiences').attr('required');

    // Button
    $('#div_id_button').show();
    $('#div2_id_button').show();
    $('#div3_id_button').show();
    $('#button_id_button').show();
    $('#span_id_button').show();
    $('#i_id_button').show();

    // Captcha

  $('#div1_id_captcha').show();
  $('#div_id_captcha').show();
  $('#span_id_captcha').show();
  $('#span2_id_captcha').show();

  }
});

$("#id_rank_choices").trigger("change");
