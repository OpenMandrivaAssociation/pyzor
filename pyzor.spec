%define name    pyzor
%define version	0.5.0
%define release	4

%define summary Pyzor is a collaborative system to detect and block spam

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPLv2
Group:          Networking/Mail
URL:            https://pyzor.org/
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	python-devel
Requires:	python
BuildArch:      noarch

%description
Pyzor is a collaborative, networked system to detect and block spam using
identifying digests of messages.

Pyzor initially started out to be merely a Python implementation of Razor, but
due to the protocol and the fact that Razor's server is not Open Source or
software libre, I decided to impelement Pyzor with a new protocol and release
the entire system as Open Source and software libre.

Since the entire system is released under the GPL, people are free to host
their own independent servers. Server peering is planned for a future release.

%prep
%setup -q

%build
%__python setup.py build

%install
rm -rf %buildroot
%__python setup.py install --root=%buildroot

# unwanted file in document dir. we packaged it in files section
rm %buildroot/%_defaultdocdir/%name/usage.html

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc COPYING README INSTALL THANKS NEWS UPGRADING
%doc docs/usage.html
%{py_puresitedir}/%{name}/
%{py_puresitedir}/*.egg-info
%defattr(755,root,root)
%_bindir/*




%changelog
* Wed Aug 05 2009 Michael Scherer <misc@mandriva.org> 0.5.0-3mdv2010.0
+ Revision: 410314
- rebuild
- remove useless spec define
- my patch was not working and is not complete, so i removed it

* Wed Aug 05 2009 Michael Scherer <misc@mandriva.org> 0.5.0-2mdv2010.0
+ Revision: 410231
- fix license
- remove warning on sha1 ( patch need to be rework before being sent to upstream )

* Thu May 14 2009 Frederic Crozat <fcrozat@mandriva.com> 0.5.0-1mdv2010.0
+ Revision: 375669
- Release 0.5.0
- Update url
- Remove patches 0, 1, 2 (merged upstream)

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.4.0-13mdv2009.1
+ Revision: 326000
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-12mdv2009.0
+ Revision: 259903
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-11mdv2009.0
+ Revision: 247750
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4.0-9mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Michael Scherer <misc@mandriva.org> 0.4.0-9mdv2007.0
+ Revision: 91365
- rebuild for new python
- use macro, and include .egg-info files
- Import pyzor

