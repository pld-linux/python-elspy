
%define 	module	elspy

Summary:	Allows to write Python code to scan email messages at SMTP-time with the Exim MTA
Summary(pl.UTF-8):	Moduł umożliwiający pisanie kodu pythonowego skanującego wiadomości w czasie SMTP w Eximie
Name:		python-%{module}
Version:	0.1.1
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://elspy.sourceforge.net/%{module}-%{version}.tar.gz
# Source0-md5:	5161553b58eedf8107048d0cd79c2360
Patch0:		%{name}-cvs20050901.patch
Patch1:		%{name}-mailpath.patch
URL:		http://elspy.sourceforge.net/
BuildRequires:	exim-devel
%pyrequires_eq	python-libs
Requires:	exim >= 4.52-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
elspy is a layer of glue code that enables you to write Python code to
scan email messages at SMTP-time with the Exim MTA (mail transport
agent). elspy also includes a small Python library with common
mail-scanning tools, including an interface to SpamAssassin and a
simple-but-effective virus detector.

%description -l pl.UTF-8
elspy to warstwa kodu sklejającego pozwalającego na pisanie w Pythonie
kodu do skanowania przesyłek pocztowych w czasie SMTP przy użyciu
Exima jako MTA (mail transport agent). elspy zawiera także małą
bibliotekę pythonową z popularnymi narzędziami do skanowania poczty,
włącznie z interfejsem do SpamAssassina i prostym lecz efektywnym
wykrywaczem wirusów.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__cc} -Wall -DDLOPEN_LOCAL_SCAN=1 %{rpmcflags} %{rpmldflags} -fPIC \
	-I%{_includedir}/exim -I%{_includedir}/python%{py_ver} \
        -lpython -shared %{module}.c -o %{module}.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/exim

%py_install

install %{module}.so $RPM_BUILD_ROOT%{_libdir}/exim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/*.py README.txt CHANGES.txt doc/API.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%attr(755,root,root) %{_libdir}/exim/%{module}.so
