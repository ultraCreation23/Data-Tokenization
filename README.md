# Privacy Preservation using Modified Data Tokenization
## Data Privacy

###Code sequence Explanation: 
1. Importing CSV file
2. Analyzing contents of the CSV files
3. Applying customized Shuffling to anonymize the names column.
   Customized Shuffling:
     ● Getting the ASCII value of every letter of the name.
     ● Shuffling the ASCII values of the entire name.
     ● Deducing ASCII character corresponding to the above change.
     ● Replacing the given names with anonymized names


4. Applying additive noise technique(perturbative masking) to the expiry date column.
   Additive noise technique:
     ● Modifying the expiry date to convert it into YY:DD:MM:HH:mm:SS
     ● Using a standard date based on the company's historical event.
     ● Finding the difference between the two dates.
     ● Converting the difference into hours, which is an enhanced version of EPOCH time.

   
5. Applying an improved version of one way tokenization to the credit card number field.
   One Way Tokenization:
     ● Concatenating “0000”, Expiry date, Current date to get a 16 digit number.
     ● Applying bitwise XOR operation on the Credit card number and the above concatenated string.
     ● Applying circular left rotation to get the final anonymized string.
     ::NOTE:: The above generated token is unique for every transaction which offers security and anonymisation in the current transaction window.

      
6. Using the data hiding technique to completely remove the extremely sensitive data from our anonymized table.


7. Generating a ”token vault” using our in-house data tokenization technique to map the data set between anonymised and input table so as to handle sensitive information carefully while ensuring all the protocols and safety standards are met.
   Token Vault Algorithm(Two way tokenization):
     ● Concatenating “00000000” and Expiry date(twice) to get a 16 digit number.
     ● Applying bitwise XOR operation to the Credit card number and the above concatenated string.
     ● Applying circular left rotation to get the token vault value and append it into the output file so as to map our dataset and establish the link
