from os import environ
import subprocess
jdk_home = environ.get('JDK_HOME')
if not jdk_home:
    jdk_home = subprocess.Popen('readlink -f /usr/bin/javac | sed "s:bin/javac::"',
            shell=True, stdout=subprocess.PIPE).communicate()[0].strip()
if not jdk_home:
    raise Exception('Unable to determine JDK_HOME')

jre_home = environ.get('JRE_HOME')
if not jre_home:
    jre_home = subprocess.Popen('readlink -f /usr/bin/java | sed "s:bin/java::"',
            shell=True, stdout=subprocess.PIPE).communicate()[0].strip()
if not jre_home:
    raise Exception('Unable to determine JRE_HOME')