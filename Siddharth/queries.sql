SELECT 
  "Year", 
  "Quarter", 
  "1st Month Emp", 
  "2nd Month Emp", 
  "3rd Month Emp" 
FROM 
  census 
WHERE 
  "Industry Name" = "Police Protection" 
  and "NAICS Code" = 92212 
  and "Area Name" = "Alameda County" 
  and "Ownership" = "State Government" 
  and "Quarter" != "Annual";
  
  
SELECT 
  "Year", 
  "Quarter", 
  "1st Month Emp", 
  "2nd Month Emp", 
  "3rd Month Emp" 
FROM 
  census 
WHERE 
  "Industry Name" = "Police Protection" 
  and "NAICS Code" = 92212 
  and "Area Name" = "Alameda County" 
  and "Ownership" = "Federal Government" 
  and "Quarter" != "Annual";
  
  
SELECT 
  "Year", 
  "Quarter", 
  "1st Month Emp", 
  "2nd Month Emp", 
  "3rd Month Emp" 
FROM 
  census 
WHERE 
  "Industry Name" = "Nursery, Garden & Farm Supply Stores" 
  and "NAICS Code" = 44422 
  and "Area Name" = "Alameda County" 
  and "Ownership" = "Federal Government" 
  and "Quarter" != "Annual";
