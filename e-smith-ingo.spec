# $Id: e-smith-ingo.spec,v 1.3 2008/06/26 05:00:03 slords Exp $

Summary: e-smith specific INGO configuration and templates.
%define name e-smith-ingo
Name: %{name}
%define version 1.2
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.2
Requires: ingo-h3 >= 1.2
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: php
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: smeserver-ingo-menuarray

%changelog 
* Wed Jun 18 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-1    
- Initial production build

* Sat May 24 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-02
- Updated to include changes in Ingo 1.2 RC3
- Re-rolled tarball

* Thu Apr 10 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-01
- Initial build
- Jump in package name to reflect new version of ingo

%description
This package adds necessary templates and configuration items
so that INGO will work properly on SME Server	

%prep
%setup

%build
 
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
