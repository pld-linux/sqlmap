Summary:	sqlmap: Automatic SQL injection tool
Name:		sqlmap
Version:	0.9
Release:	0.5
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/sqlmap/%{name}-%{version}.tar.gz
# Source0-md5:	608d5773e0925e96e618171829d679b9
URL:		http://sqlmap.sourceforge.net/
BuildRequires:	python-devel
Patch0:		%{name}-paths.patch
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_appdir		%{_datadir}/%{name}

%description
sqlmap is an open source command-line automatic SQL injection tool
developed in Python. Its goal is to detect and take advantage of SQL
injection vulnerabilities on web applications. Once it detects one or
more SQL injections on the target host, the user can choose among a
variety of options to perform an extensive back-end database
management system fingerprint, retrieve DBMS session user and
database, enumerate users, password hashes, privileges, databases,
dump entire or user's specific DBMS tables/columns, run his own SQL
statement, read specific files on the file system and more.

%prep
%setup -q -n %{name}
%patch0 -p1
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' sqlmap.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -a lib plugins shell txt xml $RPM_BUILD_ROOT%{_appdir}
install sqlmap.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_comp $RPM_BUILD_ROOT%{_appdir}
%py_postclean %{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* extra sqlmap.conf
%attr(755,root,root) %{_bindir}/sqlmap
%{_appdir}
