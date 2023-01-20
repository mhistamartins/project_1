#include <gtest/gtest.h>

/**
 A task: write a function, which simplifies a full phone number:
 - removes a code of the country (+46, +10, +1 .etc)
 -removes possible dashes (999-999-99  -> 999999)
 - removes spaces in between numbers (99 99 -> 9999)
 */

std::string SimplifyPhoneNumber(std::string phoneNumber)
{
    return phoneNumber.substr(1);
}

TEST(PhoneNumberChecks, InputIsNotOutput)
{
    //input data
    std::string fakeNumber("+50 11 999 12-35");
    //expected value
    std::string expectedNumber("0119991234");
    // logic
    std::string output = SimplifyPhoneNumber(fakeNumber);
    // comparing results
    EXPECT_NE(fakeNumber, output); //NE not equal
}


TEST(PhoneNumberChecks, ReturnErroronEmptyString)
{
    std::string fakeNumber("");
    
}

//Test case has a "Test set name" and "Test case name"
/*TEST(First_group, numbers_are_equal)
{
    EXPECT_EQ(1, 1);
}

TEST(First_group, example_1)
{
    std::string wrongInput("Error");
    std::string expectedInput("Error");
    EXPECT_EQ(wrongInput, expectedInput);
}*/