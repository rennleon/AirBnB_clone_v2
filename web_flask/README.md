# AirBnB clone - Web framework

**Usefull links**

- [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
- [Routing (except “HTTP Methods”)](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing)
- [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
- [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
- [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
- [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
- [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
- [List of Control Structures (read up to “Call”)](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
- [Template Designer Documentation](https://jinja.palletsprojects.com/en/2.9.x/templates/)
- [Jinja List of Builtin Tests](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-tests)



## 0. Hello Flask!
Write a script that starts a Flask web application:

Routes:
- `/`: display `Hello HBNB!`

```shell
$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
$
```

`File:` [0-hello_route.py](0-hello_route.py)


## 1. HBNB
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`

```shell
$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
$
```

`File:` [1-hbnb_route.py](1-hbnb_route.py)


## 2. C is fun!
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`
`/c/<text>`: display `C ` followed by the value of the text variable

```shell
$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
$
```

`File:` [2-c_route.py](2-c_route.py)


## 3. Python is cool!
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`
`/c/<text>`: display `C `, followed by the value of the text variable
`/python/(<text>)`: display `Python `, followed by the value of the text variable
The default value of text is `is cool`

```shell
$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
$
```

`File:` [3-python_route.py](3-python_route.py)


## 4. Is it a number?
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`
`/c/<text>`: display `C `, followed by the value of the text variable
`/python/(<text>)`: display `Python `, followed by the value of the text variable
The default value of text is `is cool`
`/number/<n>`: display `n is a number` only if `n` is an integer

```shell
$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
$
```

`File:` [4-number_route.py](4-number_route.py)


## 5. Number template
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`
`/c/<text>`: display `C `, followed by the value of the text variable
`/python/(<text>)`: display `Python `, followed by the value of the text variable
The default value of text is `is cool`
`/number/<n>`: display `n is a number` only if `n` is an integer
`/number_template/<n>`: display a HTML page only if `n` is an integer:
- `H1` tag: `Number: n` inside the tag `BODY`

```shell
$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
$ curl 0.0.0.0:5000/number_template/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
$
```

`File:` [5-number_template.py](5-number_template.py), [templates/5-number.html](./templates/5-number.html)


## 6. Odd or even?
Write a script that starts a Flask web application:

Routes:
`/`: display `Hello HBNB!`
`/hbnb`: display `HBNB`
`/c/<text>`: display `C `, followed by the value of the text variable
`/python/(<text>)`: display `Python `, followed by the value of the text variable
The default value of text is `is cool`
`/number/<n>`: display `n is a number` only if `n` is an integer
`/number_template/<n>`: display a HTML page only if `n` is an integer:
- `H1` tag: `Number: n` inside the tag `BODY`
`/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
- `H1` tag: `Number: n is even|odd` inside the tag `BODY`

```shell
$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
$ curl 0.0.0.0:5000/number_odd_or_even/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
$
```

`File:` [6-number_odd_or_even.py](6-number_odd_or_even.py), [templates/6-number_odd_or_even.html](./templates/6-number_odd_or_even.html)


## 7. Improve engines
Update `FileStorage`:
- Add a public method def `close(self)`: call `reload()` method for deserializing the JSON file to objects

Update `DBStorage`:
- Add a public method def `close(self)`: call `remove()` method on the private session attribute (`self.__session`) or `close()` on the class `Session`

Update `State`:
- If your storage engine is not DBStorage, add a public getter method `cities` to return the `list` of `City objects` from `storage` linked to the current `State`

`File:` [models/engine/file_storage.py](../models/engine/file_storage.py), [models/engine/db_storage.py](../models/engine/db_storage.py), [models/state.py](../models/state.py)


## 8. List of states
Write a script that starts a Flask web application:

Routes:
`/states_list`: display a HTML page:
- `H1` tag: `States`
- `UL` tag: with the list of all State objects present in DBStorage sorted by name `(A->Z)`
- `LI` tag: description of one State: `<state.id>: <B><state.name></B>`

Import this 7-dump to have some data

```shell
$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
$ cat 7-dump.sql | mysql -uroot -p
Enter password:
```

```shell
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            ...

        </UL>
    </BODY>
</HTML>
$
```

`File:` [7-states_list.py](7-states_list.py), [templates/7-states_list.html](./templates/7-states_list.html)


## 9. Cities by states
Write a script that starts a Flask web application:

Routes:
`/states_list`: display a HTML page:
- `H1` tag: `States`
- `UL` tag: with the list of all State objects present in DBStorage sorted by name `(A->Z)`
- `LI` tag: description of one State: `<state.id>: <B><state.name></B>` + `UL` tag: with the list of `City objects` linked to the State sorted by name `(A->Z)`
- `LI` tag: description of one City: `<city.id>: <B><city.name></B>`

```shell
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            ...

        </UL>
    </BODY>
</HTML>
$
```

`File:` [8-cities_by_states.py](8-cities_by_states.py), [templates/8-cities_by_states.html](./templates/8-cities_by_states.html)


## 10. States and State
Write a script that starts a Flask web application:
Routes:
`/states_list`: display a HTML page:
- `H1` tag: `States`
- `UL` tag: with the list of all State objects present in DBStorage sorted by name `(A->Z)`
- `LI` tag: description of one State: `<state.id>: <B><state.name></B>`

`/states/<id>`: display a HTML page:
- If a `State object` is `found` with this `id`:
 - `H1` tag: `State: `
 - `H3` tag: `Cities:`
 - `UL` tag: with the `list` of `City objects` linked to the State sorted by name `(A->Z)`
 - `LI` tag: description of one City: `<city.id>: <B><city.name></B>`
- Otherwise:
 - H1 tag: `Not found!`

```shell
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```shell
$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            ...

        </UL>

    </BODY>
</HTML>
$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
$
```

`File:` [9-states.py](9-states.py), [templates/9-states.html](./templates/9-states.html)


## 11. HBNB filters
Write a script that starts a Flask web application:

Routes:
`/hbnb_filters`: display a HTML page

Import this 10-dump to have some data

```shell
$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
$ cat 10-dump.sql | mysql -uroot -p
Enter password:
```

```shell
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

`File:` [10-hbnb_filters.py](10-hbnb_filters.py), [templates/10-hbnb_filters.html](./templates/10-hbnb_filters.html), [static/](./static/)


## 12. HBNB is alive!
Write a script that starts a Flask web application:

Routes:
`/hbnb`: display a HTML page

Import this 100-dump to have some data

```shell
$ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
$ cat 100-dump.sql | mysql -uroot -p
Enter password:
```

```shell
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

`File:` [100-hbnb.py](100-hbnb.py), [templates/100-hbnb.html](./templates/100-hbnb.html), [static/](./static/)
