%define name pyctd
%define version 0.4.4
%define rel 4

Summary: A service for monitoring and altering Netfilter connections
Name: %{name}
Version: %{version}
Release: %mkrel %rel
Source0: %{name}-%{version}.tar.gz
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
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/auto_daemon.py*




%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.4.4-4mdv2011.0
+ Revision: 592430
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.4-3mdv2010.0
+ Revision: 441985
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.4.4-2mdv2009.1
+ Revision: 325947
- rebuild

* Tue Feb 19 2008 Michael Scherer <misc@mandriva.org> 0.4.4-1mdv2008.1
+ Revision: 173047
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Michael Scherer <misc@mandriva.org> 0.4.2-1mdv2008.1
+ Revision: 97699
- new version 0.4.2

* Mon Apr 23 2007 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2008.0
+ Revision: 17272
- 0.2


* Tue Dec 12 2006 Michael Scherer <misc@mandriva.org> 0.1-2mdv2007.0
+ Revision: 95743
- Rebuild for python 2.5

* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.1
+ Revision: 84822
- buildrequires python-devel
- initial pyctd release
- Create pyctd

