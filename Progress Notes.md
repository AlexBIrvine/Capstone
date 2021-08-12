## <u>**8/11**</u>

<u>**What this needs to do**</u>:

- Read in csv file
- Clean & prepare data
- Be a desktop GUI
- Use K-means clustering and logistic regression
- Display other data just caught by the dataset
- Enable logging
- Have a crash report
- Have unit tests
- Predict the accuracy
- Store logs with encryption?

<u>**What tools do I need for these actions?**</u>

<u>**GUI**</u>: PyQT 6  
<u>**CSV**</u>: Pandas/built-in  
<u>**Modeling**</u>: skLearn  
<u>**Visualize data**</u>: PyQT charts  
<u>**Unit testing**</u>: unittest/pytest
<u>**logging**</u>: logging  
<u>**Crash reporting**</u>: Try-catch the main method  
<u>**Configuration variables**</u>: Classes, YAML?
<u>**Encrypted storage**</u>: ??
<u>**Print to PDF**</u>: ??

<u>**What actions do I need to take?**</u>:

1. Read in the CSV file and prepare data
   1. Load the csv file
   2. Remove the following columns:
      - One
      - Two
   3. Match fuel type to make
   4. Fill in empty fuel types
   5. Remove rows without ratings
   6. (Do I care about missing daily rates?)
2. Feed data into models
   1. Many steps, research soon
3. Verify accuracy of data
4. Build the GUI
   1. Login screen, admin/admin saved in the config for the name/password
   2. 3 sections: K-Means, Logistic, other data. These sections are tabs at the top.
   3. Logistic: Line the input variable option on the bottom, update graph when variable changes
   4. K-Means: Have button on bottom (mirroring the logistic) to switch between clusters.
   5. the rest: Mirror K-Means, display appropriate graphs. Also show "stats"? (number of records, most common car, average vehicle year, etc.,)
   6. Print report button for Logistic and K-means?
5. Create a logger & crash report
   1. Create a YAML config file that sets up:
      - Formatted strings
      - A console, file & email logger
   2. Record the following events:
      - User login
      - User actions
      - User closing application
      - Any exceptions
   3. Save all logs to a file
   4. Email exception logs with log file attachment
   5. Open new program (crash report) when program exits?
   6. Encrypt logs?
6. Create unit tests
   1. use pytest for each method
7. Encryption?
