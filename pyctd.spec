%define name pyctd
%define version 0.1
%define rel 2

Summary: A service for monitoring and altering Netfilter connections
Name: %{name}
Version: %{version}
Release: %mkrel %rel
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://software.inl.fr/trac/trac.cgi/wiki/%{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
Requires: pynetfilter_conntrack

%description
pyctd is a XML-RPC service for monitoring and altering Netfilter
connections for network admins.

It has the following functionnalities :
* Connections listing (with byte rate of connections)
* Entries removal
* Modification of mark and timeout 

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
echo y | python setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}.py
%dir %{py_puresitedir}/_%{name}
%{py_puresitedir}/_%{name}/*.py*
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/auto_daemon.py*


