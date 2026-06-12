# API Reference

## `parse(input_str)`
Parses a JSON string into a C-style struct.
- **Input**: `const char*`
- **Output**: `bool` (Success/Failure)

## `serialize(data_struct)`
Converts a struct back to a JSON string.
- **Input**: `struct NanoJsonData`
- **Output**: `char*` (Buffer)
