# Pulumi-Demo
Pulumi-Demo-1
Python :
C:\Python\Python310

PIP :
C:\Python\Python310\Lib\site-packages\pip

PULUMI Zip download for Windows:

https://get.pulumi.com/releases/sdk/pulumi-v3.37.2-windows-x64.zip?_gl=1*afxlxl*_ga*MTc2NTE0NTg2Ny4xNjYwMjgzMjQ3*_ga_FQHG5CVY2D*MTY2MDI4NTgzMy4yLjAuMTY2MDI4NTgzMy42MA..

Add to environment variables:

Windows + R - > sysdm.cpl  -> Advanced -> Environment Variables -> Add ->

Old PATH:
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps

Add New PATH for Python and Pulumi

=============Python Virtual Environment===========
C:\Users\Chirag Sharma>pip version
ERROR: unknown command "version"

C:\Users\Chirag Sharma>pip -version

Usage:
  pip <command> [options]

no such option: -e

C:\Users\Chirag Sharma>python -m venv c:\Venv_PY\PulumiPY

C:\Users\Chirag Sharma> c:\Venv_PY\PulumiPY\activate.bat
'c:\Venv_PY\PulumiPY\activate.bat' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Chirag Sharma> c:\Venv_PY\PulumiPY\scripts\activate.bat

(PulumiPY) C:\Users\Chirag Sharma>



To deactivate Virtual environment 

deactivate

============================================

==================>>>>>Install Pulumi for OCI on Python<<<<<===============

python -m pip install pulumi_oci 

(PulumiPY) C:\Users\Chirag Sharma>python -m pip install pulumi_oci
Collecting pulumi_oci
  Downloading pulumi_oci-0.1.1.tar.gz (3.3 MB)
     ---------------------------------------- 3.3/3.3 MB 1.8 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting parver>=0.2.1
  Downloading parver-0.3.1-py2.py3-none-any.whl (14 kB)
Collecting pulumi<4.0.0,>=3.0.0
  Downloading pulumi-3.37.2-py2.py3-none-any.whl (166 kB)
     ---------------------------------------- 166.1/166.1 kB 829.0 kB/s eta 0:00:00
Collecting semver>=2.8.1
  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)
Collecting arpeggio~=1.7
  Downloading Arpeggio-1.10.2-py2.py3-none-any.whl (54 kB)
     ---------------------------------------- 54.9/54.9 kB 2.8 MB/s eta 0:00:00
Collecting six~=1.13
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting attrs>=19.2
  Downloading attrs-22.1.0-py2.py3-none-any.whl (58 kB)
     ---------------------------------------- 58.8/58.8 kB 622.5 kB/s eta 0:00:00
Collecting dill~=0.3
  Downloading dill-0.3.5.1-py2.py3-none-any.whl (95 kB)
     ---------------------------------------- 95.8/95.8 kB 920.3 kB/s eta 0:00:00
Collecting grpcio==1.47
  Downloading grpcio-1.47.0-cp310-cp310-win_amd64.whl (3.5 MB)
     ---------------------------------------- 3.5/3.5 MB 1.8 MB/s eta 0:00:00
Collecting protobuf~=4.21
  Downloading protobuf-4.21.5-cp310-abi3-win_amd64.whl (525 kB)
     ---------------------------------------- 525.5/525.5 kB 2.4 MB/s eta 0:00:00
Collecting pyyaml~=5.3
  Downloading PyYAML-5.4.1.tar.gz (175 kB)
     ---------------------------------------- 175.1/175.1 kB 10.3 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Using legacy 'setup.py install' for pulumi_oci, since package 'wheel' is not installed.
Building wheels for collected packages: pyyaml
  Building wheel for pyyaml (pyproject.toml) ... done
  Created wheel for pyyaml: filename=PyYAML-5.4.1-cp310-cp310-win_amd64.whl size=45655 sha256=c9d58258325748b2b607c193890fac3655ab401f3d14e9e439286712afc5684e
  Stored in directory: c:\users\chirag sharma\appdata\local\pip\cache\wheels\c7\0d\22\696ee92245ad710f506eee79bb05c740d8abccd3ecdb778683
Successfully built pyyaml
Installing collected packages: arpeggio, six, semver, pyyaml, protobuf, dill, attrs, parver, grpcio, pulumi, pulumi_oci
  Running setup.py install for pulumi_oci ... done
Successfully installed arpeggio-1.10.2 attrs-22.1.0 dill-0.3.5.1 grpcio-1.47.0 parver-0.3.1 protobuf-4.21.5 pulumi-3.37.2 pulumi_oci-0.1.1 pyyaml-5.4.1 semver-2.13.0 six-1.16.0

[notice] A new release of pip available: 22.2.1 -> 22.2.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(PulumiPY) C:\Users\Chirag Sharma>


=============Using new compartment login to pulumi in browser and create a new venv==========
C:\Users\Chirag Sharma\Pulumi-test>pulumi new python
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :
We've launched your web browser to complete the login process.

Waiting for login to complete...


  Welcome to Pulumi!

  Pulumi helps you create, deploy, and manage infrastructure on any cloud using
  your favorite language. You can get started today with Pulumi at:

      https://www.pulumi.com/docs/get-started/

  Tip of the day: Resources you create with Pulumi are given unique names (a randomly
  generated suffix) by default. To learn more about auto-naming or customizing resource
  names see https://www.pulumi.com/docs/intro/concepts/resources/#autonaming.


This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (Pulumi-test)
project description: (A minimal Python Pulumi program) OCI-LAB-TEST-1
Created project 'Pulumi-test'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'

Failed to resolve python version command: exec: "C:\\Users\\Chirag Sharma\\Pulumi-test\\venv\\Scripts\\python.exe": file does not exist

Installing dependencies...

Creating virtual environment...
Finished creating virtual environment
Updating pip, setuptools, and wheel in virtual environment...
Requirement already satisfied: pip in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (22.2.1)
Collecting pip
  Downloading pip-22.2.2-py3-none-any.whl (2.0 MB)
     ---------------------------------------- 2.0/2.0 MB 13.0 MB/s eta 0:00:00
Requirement already satisfied: setuptools in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (63.2.0)
Collecting setuptools
  Downloading setuptools-65.0.1-py3-none-any.whl (1.2 MB)
     ---------------------------------------- 1.2/1.2 MB 19.2 MB/s eta 0:00:00
Collecting wheel
  Using cached wheel-0.37.1-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel, setuptools, pip
  Attempting uninstall: setuptools
    Found existing installation: setuptools 63.2.0
    Uninstalling setuptools-63.2.0:
      Successfully uninstalled setuptools-63.2.0
  Attempting uninstall: pip
    Found existing installation: pip 22.2.1
    Uninstalling pip-22.2.1:
      Successfully uninstalled pip-22.2.1
Successfully installed pip-22.2.2 setuptools-65.0.1 wheel-0.37.1
Finished updating
Installing dependencies in virtual environment...
Collecting pulumi<4.0.0,>=3.0.0
  Using cached pulumi-3.37.2-py2.py3-none-any.whl (166 kB)
Collecting grpcio==1.47
  Using cached grpcio-1.47.0-cp310-cp310-win_amd64.whl (3.5 MB)
Collecting semver~=2.8
  Using cached semver-2.13.0-py2.py3-none-any.whl (12 kB)
Collecting six~=1.12
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting pyyaml~=5.3
  Using cached PyYAML-5.4.1-cp310-cp310-win_amd64.whl
Collecting protobuf~=4.21
  Using cached protobuf-4.21.5-cp310-abi3-win_amd64.whl (525 kB)
Collecting dill~=0.3
  Using cached dill-0.3.5.1-py2.py3-none-any.whl (95 kB)
Installing collected packages: six, semver, pyyaml, protobuf, dill, grpcio, pulumi
Successfully installed dill-0.3.5.1 grpcio-1.47.0 protobuf-4.21.5 pulumi-3.37.2 pyyaml-5.4.1 semver-2.13.0 six-1.16.0
Finished installing dependencies
Finished installing dependencies

Your new project is ready to go!

To perform an initial deployment, run 'pulumi up'


C:\Users\Chirag Sharma\Pulumi-test>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Chirag Sharma\Pulumi-test>ls -lrt
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Chirag Sharma\Pulumi-test>ll
'll' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Chirag Sharma\Pulumi-test>dir
 Volume in drive C is System
 Volume Serial Number is 660C-2059

 Directory of C:\Users\Chirag Sharma\Pulumi-test

16-08-2022  11:10    <DIR>          .
16-08-2022  11:10    <DIR>          ..
16-08-2022  11:09                14 .gitignore
16-08-2022  11:09               102 Pulumi.yaml
16-08-2022  11:09                22 requirements.txt
16-08-2022  11:10    <DIR>          venv
16-08-2022  11:09                48 __main__.py
               4 File(s)            186 bytes
               3 Dir(s)  162,513,899,520 bytes free

C:\Users\Chirag Sharma\Pulumi-test>cd venv

C:\Users\Chirag Sharma\Pulumi-test\venv>dir
 Volume in drive C is System
 Volume Serial Number is 660C-2059

 Directory of C:\Users\Chirag Sharma\Pulumi-test\venv

16-08-2022  11:10    <DIR>          .
16-08-2022  11:10    <DIR>          ..
16-08-2022  11:10    <DIR>          Include
16-08-2022  11:10    <DIR>          Lib
16-08-2022  11:10                74 pyvenv.cfg
16-08-2022  11:10    <DIR>          Scripts
               1 File(s)             74 bytes
               5 Dir(s)  162,497,138,688 bytes free


C:\Users\Chirag Sharma\Pulumi-test\venv>cd C:\Users\Chirag Sharma\Pulumi-test\venv\

C:\Users\Chirag Sharma\Pulumi-test\venv>cd Scripts

C:\Users\Chirag Sharma\Pulumi-test\venv\Scripts>activate

(venv) C:\Users\Chirag Sharma\Pulumi-test\venv\Scripts>cd ../..

(venv) C:\Users\Chirag Sharma\Pulumi-test>dir
 Volume in drive C is System
 Volume Serial Number is 660C-2059

 Directory of C:\Users\Chirag Sharma\Pulumi-test

16-08-2022  11:10    <DIR>          .
16-08-2022  11:10    <DIR>          ..
16-08-2022  11:09                14 .gitignore
16-08-2022  11:09               102 Pulumi.yaml
16-08-2022  11:09                22 requirements.txt
16-08-2022  11:10    <DIR>          venv
16-08-2022  11:09                48 __main__.py
               4 File(s)            186 bytes
               3 Dir(s)  162,496,827,392 bytes free
(venv) C:\Users\Chirag Sharma\Pulumi-test> type requirements.txt
pulumi>=3.0.0,<4.0.0
pulumi_oci                         <-------------- Note the cloud specific requirement


(venv) C:\Users\Chirag Sharma\Pulumi-test>pip install -r requirements.txt
Requirement already satisfied: pulumi<4.0.0,>=3.0.0 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from -r requirements.txt (line 1)) (3.37.2)
Collecting pulumi_oci
  Downloading pulumi_oci-0.2.0.tar.gz (3.6 MB)
     ---------------------------------------- 3.6/3.6 MB 10.0 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: pyyaml~=5.3 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (5.4.1)
Requirement already satisfied: grpcio==1.47 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (1.47.0)
Requirement already satisfied: semver~=2.8 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (2.13.0)
Requirement already satisfied: six~=1.12 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (1.16.0)
Requirement already satisfied: dill~=0.3 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (0.3.5.1)
Requirement already satisfied: protobuf~=4.21 in c:\users\chirag sharma\pulumi-test\venv\lib\site-packages (from pulumi<4.0.0,>=3.0.0->-r requirements.txt (line 1)) (4.21.5)
Collecting parver>=0.2.1
  Using cached parver-0.3.1-py2.py3-none-any.whl (14 kB)
Collecting arpeggio~=1.7
  Using cached Arpeggio-1.10.2-py2.py3-none-any.whl (54 kB)
Collecting attrs>=19.2
  Using cached attrs-22.1.0-py2.py3-none-any.whl (58 kB)
Building wheels for collected packages: pulumi_oci
  Building wheel for pulumi_oci (setup.py) ... done
  Created wheel for pulumi_oci: filename=pulumi_oci-0.2.0-py3-none-any.whl size=5792805 sha256=f01e800190cc84cc7ae6ab26272d291b218f0d34cbb41520343da2bba78018ef
  Stored in directory: c:\users\chirag sharma\appdata\local\pip\cache\wheels\93\86\be\c92c06487166ce57969c3499e5b4fc9db82dd05983e4503c5b
Successfully built pulumi_oci
Installing collected packages: arpeggio, attrs, parver, pulumi_oci
Successfully installed arpeggio-1.10.2 attrs-22.1.0 parver-0.3.1 pulumi_oci-0.2.0



=======================================Pulumi COnfiguration======================
Compartment OCI-LAB-32 OCID : ocid1.compartment.oc1..aaaaaaaax6uvmemkbtkybkq3omoh3ikrw7cmeywfmm2hinhgvhp2z4r7cvha

https://console.us-ashburn-1.oraclecloud.com/identity/compartments/ocid1.compartment.oc1..aaaaaaaax6uvmemkbtkybkq3omoh3ikrw7cmeywfmm2hinhgvhp2z4r7cvha

Pulumi OCI LAB Token : pul-e3366a703bbc1d452d951202dc996f7096073778

OCI Auth Token : ########
API Fingerprint: ########

SSH Key Fingerprint : ssh-rsa 2048 SHA256:dRY7KbWhQ+eZ8Ezv6ikuD+cfzwqe9zQYdbIsOPy/o38

C:\Users\Chirag Sharma>echo %%PULUMI_ACCESS_TOKEN%%    <------------ set in environment variables
%###################################%

pulumi stack select chirag09491/Pulumi-test/dev
-----
Config FIle:  Save this file as ~/.oci/config

[DEFAULT]
user=ocid1.user.oc1..##################################
fingerprint=#########################################
tenancy=ocid1.tenancy.oc1..################################
region=us-ashburn-1
key_file=C:\Users\Chirag Sharma\.oci\oci_api_key.pem # TODO
-----
Generate RSA Keys:

winpty openssl genrsa -out oci_api_key.pem -aes128 -passout stdin 2048

winpty openssl rsa -pubout -in oci_api_key.pem -out oci_api_key_public.pem

Fingetprint : Use fingerprint after importing Public Key to OCI API Signing keys
 
 winpty openssl rsa -pubout -outform DER -in oci_api_key.pem | openssl md5 -c
stdout is not a tty
(stdin)= ############################    <<<<<< Not required


=================Configuration:

pulumi config set oci:tenancyOcid "ocid1.tenancy.oc1..########################" --secret
pulumi config set oci:compartmentOcid "ocid1.compartment.oc1..###################################a" --secret
pulumi config set oci:userOcid "ocid1.user.oc1..##############################" --secret
pulumi config set oci:fingerprint "####################" --secret
pulumi config set oci:region "us-ashburn-1"
pulumi config set privateKeyPath --secret "C:\Users\Chirag Sharma\.oci\oci_api_key.pem"   
=============================================

========================INstance creation

Name
AD
Compartment
image
	image version
shape
	compatible shapes (should be compatible with image ver.)
	VM or BM	
	OCPU, Memory, Bandwidth, Max VNICs
Network
	VCN -> Name of the VCN
	subnet -> from VCN
	RSA Key pair  (to be generated beforehand on local machine)
STorage
	Boot Volume
		size
		Encryption-in-transit enable/disable
		
		
==============Remaining items for connectivity=========
Internet Gateway route table
ingress and egress rules -> for subnet
attach route table to internet gateway
=======destroy specific pulumi resource======
check resource urn from pulumi website
run below from cmd

pulumi destroy -t urn:pulumi:dev::Pulumi-test::oci:Core/securityList:SecurityList::Security_list_Chirag
	
	
=========connecting from git bash=====
Chirag Sharma@CHIRSHAR-4M49R73 MINGW64 ~/.ssh
$ pwd
/c/Users/Chirag Sharma/.ssh

Chirag Sharma@CHIRSHAR-4M49R73 MINGW64 ~/.ssh
$ ssh -i ssh-rsa opc@xxx.xxx.xxx.xxx


	
	
	
(venv) C:\Users\Chirag Sharma\Pulumi-test>
