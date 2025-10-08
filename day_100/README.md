Today, I resolved the **Outdated problem** from **Harvard's CS50P Week 3**!  
This problem focused on **date parsing**, **format conversion**, and **input validation** to convert dates to ISO 8601 format.  

---

## ✅ Problem Overview  

- 📅 **Date Format Conversion** → Convert MM/DD/YYYY or "Month DD, YYYY" to YYYY-MM-DD.  
- 🔍 **Format Detection** → Identify numeric vs text date formats.  
- ✅ **Input Validation** → Ensure valid months (1-12) and days (1-31).  
- 🔢 **Zero-Padding** → Format output with leading zeros (09 instead of 9).  
- 🔄 **Error Handling** → Re-prompt on invalid input.  

---

## 🎯 Problem Solved

### Date Format Converter
Built a program that:
- Accepts two date formats: `9/8/1636` or `September 8, 1636`
- Validates month and day ranges
- Converts month names to numbers
- Outputs in ISO 8601 format: `YYYY-MM-DD`
- Re-prompts on invalid input

**Examples**:
```
Date: 9/8/1636
1636-09-08

Date: September 8, 1636
1636-09-08

Date: December 25, 2000
2000-12-25
```

**Invalid Inputs (Re-prompt)**:
```
Date: 23/6/1912     (invalid month)
Date: December 32, 1999     (invalid day)
Date: September 8 1636      (missing comma)
Date: 9/8/1636
1636-09-08
```

---

## 💭 Daily Reflection  

This problem taught me about **date parsing** and **handling multiple input formats**.  
The key insight was detecting format types using `/` and `,`, then validating ranges before converting to standardized ISO 8601 format.  

> "Old dates are like old code — they need to be converted to modern standards to work seamlessly!" 📅✨