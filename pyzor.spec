%define name    pyzor
%define version	0.4.0
%define release	%mkrel 9

%define summary Pyzor is a collaborative system to detect and block spam

%define	python_ver   %pyver

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Networking/Mail
URL:            http://pyzor.sourceforge.net/
Source0:        %name-%version.tar.bz2
Patch0:		%name-python_path.patch
Patch1:		%name-handle_digest_is_none.patch
Patch2:		%name-handle_unknown_encoding.patch
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
%patch0 -p0 -b .%name-python_patch.patch
%patch1 -p0 -b .%name-handle_digest_is_none.patch
%patch2 -p0 -b .%name-handle_unknown_encoding.patch


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
%doc COPYING README INSTALL ChangeLog THANKS NEWS UPGRADING
%doc docs/usage.html
%{py_puresitedir}/%{name}/
%{py_puresitedir}/*.egg-info
%defattr(755,root,root)
%_bindir/*


