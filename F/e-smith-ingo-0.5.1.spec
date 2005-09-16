Summary: e-smith specific INGO configuration and templates.
%define name e-smith-ingo
Name: %{name}
%define version 0.5.1
%define release 01
Version: %{version}
Release: %{release}
License: GPL
Vendor: SME Server
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: SME Server Developers <smeserver-developer@sourceforge.net>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: ingo-h3 >= 1.0.1
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: php
Requires: php-pear
Requires: pear-date
Requires: pear-db
Requires: pear-file
Requires: pear-log
Requires: pear-mail
Requires: pear-mail_mime
AutoReqProv: no

%changelog
* Wed Aug 31 2005 Greg Swallow <gregswallow@skynetonline.ca>
- [0.5.1-01]
- initial release

%description
This package adds necessary templates and configuration items
so that INGO will work properly.

%prep
%setup

%build
for file in conf.php backends.php prefs.php
do 
    mkdir -p root/etc/e-smith/templates/home/httpd/html/horde/ingo/config/$file
    ln -s /etc/e-smith/templates-default/template-begin-php \
         root/etc/e-smith/templates/home/httpd/html/horde/ingo/config/$file/template-begin
    ln -s /etc/e-smith/templates-default/template-end-php \
         root/etc/e-smith/templates/home/httpd/html/horde/ingo/config/$file/template-end
done
 
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
