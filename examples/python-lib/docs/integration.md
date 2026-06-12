---
ai-context:
  topic: "NanoJSON Integration"
  prerequisites: ["C99 Compiler", "Standard Lib"]
  critical-warning: "The `serialize` function requires a pre-allocated buffer of at least 512 bytes to avoid overflow."
---

# Integration Guide

To integrate NanoJSON, simply include `nanojson.h` in your project.

### Basic Usage
```c
char* json = "{ \"temp\": 22 }";
if (parse(json)) {
    printf("Success!");
}
```
