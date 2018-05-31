FROM python:3.5-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk --no-cache upgrade && apk --no-cache add chromium chromium-chromedriver

EXPOSE 8080

ENV CHROME_DRIVER /usr/bin/chromedriver
ENV LI_AT AQEDARHxb2gF0opMAAABVDR3aSEAAAFj0HOwwk4AY6JgyFZUIwdql_Fuw1yq8oarUL-Z3vM0sWOgapjYyutGrY4s0bDLLAWcn7dDRci2B9JJCHdov_GsuIELCFfxt2w8mHGB4LxEkjCcqYLqSyfh8sYc


ENTRYPOINT ["python"]
CMD ["app.py"]
