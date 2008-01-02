Summary:	LTSP hardware lists
Name:		ltsp-hwlists
Version:	0.02
Release:	%mkrel 1
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


