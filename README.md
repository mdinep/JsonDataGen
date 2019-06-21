README

1.Data IO
Config files for this tool can reside anywhere.
The file to use must be selected before data can be generated.
The default location for these files is in the same directory as this tool.
the input CV and output directory for the dataset are the same.

2. Config File
The config file used by this script uses standard Python ConfigParser notation.
There is an empty sample file provided called sample.conf
This file is located at the same location as that of the script.
This file provides config values and datatype override information for data fields.
By default, field values are generated either as strings on based on SQL field types from input.
Ths config is broken up into two sections

	A. INPUT
	Values are randomly generated or assigned for all fields.
	These overrides allow for explicit typing of the random values.
	The config values for these is a comma separated list.
	The input section has the following entry fields:
	header - a boolean value for whether the input data has a header line to be skipped
	file - the name of the input file to use
		this should be a CSV
		format is covered in section 3
	pathColumn - the column number where the JSON path of a field is located
		numbering starts at 1  and is counted left to right
		this is a required config value
	fieldColumn - the column where the JSON field name is located 
		numbering starts at 1  and is counted left to right
		this is a required config value
	typeColumn - the column where the field's type is located
		numbering starts at1  and is counted left to right
		types recognized are SQL database types, such as NUMBER and VARCHAR
		this is NOT a required config value
		if this is not supplied, all fields default to VARCHAR, aka string
		field type overrides from the config vile take precedence over the column types
	integers- data fields that are integer values
		this is an override for fields that are not typed as NUMBER in the source
	dates - data fields that are dates
		this is separate from datetimes
		datetime fields should not be included here
	booleans - data fields that are booleans
	phone - data fields that are phone numbers
		this currently only generates US-formatted phone numbers
	month - data fields that are months
	day -  - data fields that are days
	year -  - data fields that are years
	time - data fields that are times
		thi is separate from datetime
	datetime -  - data fields that are datetimes
		this will generate a random date and time and combine them
		format is 24 hour Zulu time yyyy-mm-dd'T'hh:mm:ss.sssZ
	uid - data fields that are unique IDs
		this generates a random alphanumberic string
	ssn - data fields that are social security numbers
		the output for this type is delimited by a configurable character delimiter
	latitude - data fields that are latitudes
	longitude - data fields that are longitudes
	LatLon - data fields that contain both latitudeand longitude values
		produces randomly generated latitude and longitude values
		values are separated by a comma

	B. OUTPUT
	This is a much smaller config section
	All entries are specific to output location and formatting of data
	The output section has the following fields:
	file - The output file for data
		this must include file extension
	maxUIDLength - the character length for randomly generated UIDs
	ssnDivider - the delimiter character for randomly generated SSNs
		if no value is provided, the ssn will just be a 9 digit string
	phoneDivider - the delimiter character for randomly generated phone numbers
		if no value is provided, the phone number will just be a 10 digit string
	staticValues - This is a map of specific fields that should have explicit values assigned
		formatting for this is {"key1":"value1","key2":"value2"}

3. Input File
The expected input file for this script is a csv.
The csv requires at least two columns, though can effectively use a third (more will be ignored).
The columns do not haveot be ordered, as their column number is defined in the config.
The recognized columns are as follows:

	A. JSON Branch path
	This column is used to build the full JSON path for each output field.
	In a flattened JSON, this would be the key, minus hte fieldname at the end.	

	B. Field Name
	This is the actual field name used to build the JSON path.
	This combined with the above creates a full path in JSON to a key.
	The full path is expressed with dot notaiton in a flattened JSON on output.

	C. Datatype
	This is the datatype for the field value to generate.
	This uses SQL database types such as VARCHARm NUMBER, and DATE.
	This column is used to programatically generate correct values
		if a field name is not present in the config file.
	The only types that are currently supported are NUMBER, DATE, and CHAR
	CHAR must have a field size (expressed as CHAR(1))
	All other non-config-overridden datatypes default to VARCHAR
	For non-database datasets, NUMBER, CHAR, and DATE fields should have a value set in
		this column to avoid building a huge config override list
	

4. Output
The defalt output from this tool, as mentioned earlier, is the smae as the location of the script.
This output directory can be changed during runtime.
The output is a flattened JSON of key-vlaue pairs.
All fields from the input CSV should be accurately represented in the output.
The keys are the full JSON path for all fields, expressed with dot notation.
The file generated for output is meant to be run through another tool to be unflattened into proper structure.

5. Extensibility
COMING SOON
