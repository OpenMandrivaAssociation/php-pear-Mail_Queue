%define		_class		Mail
%define		_subclass	Queue
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.7
Release:	4
Summary:	Put mails in queue and send them later in background
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Mail_Queue/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Class for handle mail queue managment. Wrapper for PEAR::Mail and
PEAR::DB. Could load, save and send saved mails in background and also
backup some mails. Mail queue class put mails in a temporary container
waiting to be fed to the MTA (Mail Transport Agent) and send them
later (eg. every few minutes) by crontab or in other way.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2012.0
+ Revision: 742038
- fix major breakage by careless packager

* Sun Jul 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-1
+ Revision: 690176
- 1.2.7

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-2
+ Revision: 679391
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.6-1mdv2011.0
+ Revision: 594493
- update to new version 1.2.6

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-4mdv2010.1
+ Revision: 470149
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Nov 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-3mdv2010.1
+ Revision: 463811
- use rpm filetriggers to register starting from mandriva 2010.1

* Sat Oct 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-2mdv2010.0
+ Revision: 453176
- fix dependencies

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-1mdv2010.0
+ Revision: 450210
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-3mdv2010.0
+ Revision: 441294
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdv2009.1
+ Revision: 322356
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 278926
- update to new version 1.2.2

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-8mdv2009.0
+ Revision: 236918
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.1.3-7mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-7mdv2007.0
+ Revision: 82084
- Import php-pear-Mail_Queue

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdk
- initial Mandriva package (PLD import)

