# MVC flask 

## Structure of a website 
- HTML - < HyperText markup Language>
```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
``` 

- CSS - {Cascading Style Sheets}
```
body {
  background-color: lightblue;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
```  

- JS -  Javascript
```
function storeNames() { return arguments; }
// If we execute the following line in the console:
storeNames("Mulder", "Scully", "Alex Kryceck");
// The output will be { '0': 'Mulder', '1': 'Scully', '2': 'Alex Kryceck' }
```

## Model-View-Controller(MVC)
1. A user requests to view a page by entering a URL.
2. The **Controller** receives that request.
3. It uses the **Models** to retrieve all of the necessary data, organizes it, and sends it off to the...
4. **View**, which then uses that data to render the final webpage presented to the the user in their browser.
   

![MVC](https://files.realpython.com/media/mvc_diagram_with_routes.e12c5b982ac8.png)

![Flask](https://devopedia.org/images/article/140/9072.1547744489.png)
