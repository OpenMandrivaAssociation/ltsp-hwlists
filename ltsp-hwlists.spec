Summary:	LTSP hardware lists
Name:		ltsp-hwlists
Version:	0.02
Release:	%mkrel 4
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
Source0:	pci_scan-lists.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

%description
This package contains LTSP hardware lists for use with pci_scan. It includes a
network card list, video card list, sound card list and usb controller list.

%prep

%setup -q -c -T -a0

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}

install -m0644 audiolist %{buildroot}%{_sysconfdir}
install -m0644 audiolist.alsa %{buildroot}%{_sysconfdir}
install -m0644 audiolist.bestdriver %{buildroot}%{_sysconfdir}
install -m0644 niclist %{buildroot}%{_sysconfdir}
install -m0644 usblist %{buildroot}%{_sysconfdir}
install -m0644 vidlist %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/audiolist
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/audiolist.alsa
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/audiolist.bestdriver
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/niclist
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/usblist
%attr(0644,root,root) %config (noreplace) %{_sysconfdir}/vidlist




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.02-4mdv2010.0
+ Revision: 429880
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-3mdv2009.0
+ Revision: 251501
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.02-1mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2007.0
+ Revision: 117097
- Import ltsp-hwlists

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package (mille-xterm import)

