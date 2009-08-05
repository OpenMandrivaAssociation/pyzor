%define name    pyzor
%define version	0.5.0
%define release	%mkrel 2

%define summary Pyzor is a collaborative system to detect and block spam

%define	python_ver   %pyver

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPLv2
Group:          Networking/Mail
URL:            http://pyzor.org/
Source0:        %name-%version.tar.bz2
# error fixed in trunk, 
# http://pyzor.svn.sourceforge.net/viewvc/pyzor?view=rev&revision=226
Patch0:         pyzor-no_warning_python_26.diff
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
%patch0 -p0

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


