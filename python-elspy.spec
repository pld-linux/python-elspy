
%define 	module	elspy

Summary:	Allows to write Python code to scan email messages at SMTP-time with the Exim MTA
Name:		python-%{module}
Version:	0.1.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://elspy.sourceforge.net/%{module}-%{version}.tar.gz
# Source0-md5:	5161553b58eedf8107048d0cd79c2360
URL:		http://elspy.sourceforge.net/
BuildRequires:	acl-devel
%pyrequires_eq	python-libs
Requires:	exim >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
elspy is a layer of glue code that enables you to write Python code to
scan email messages at SMTP-time with the Exim MTA (mail transport
agent). elspy also includes a small Python library with common
mail-scanning tools, including an interface to SpamAssassin and a
simple-but-effective virus detector.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/*.py
%dir %{py_sitescriptdir}/%{module}
%attr(755,root,root) %{py_sitescriptdir}/%{module}/*.py[co]
