Summary:	LTSP hardware lists
Name:		ltsp-hwlists
Version:	0.02
Release:	5
License:	GPLv2+
Group:		System/Servers
Url:		http://www.ltsp.org
Source0:	pci_scan-lists.tar.bz2
BuildArch:	noarch

%description
This package contains LTSP hardware lists for use with pci_scan. It includes a
network card list, video card list, sound card list and usb controller list.

%files
%config(noreplace) %{_sysconfdir}/audiolist
%config(noreplace) %{_sysconfdir}/audiolist.alsa
%config(noreplace) %{_sysconfdir}/audiolist.bestdriver
%config(noreplace) %{_sysconfdir}/niclist
%config(noreplace) %{_sysconfdir}/usblist
%config(noreplace) %{_sysconfdir}/vidlist

#----------------------------------------------------------------------------

%prep
%setup -q -c -T -a0

%build

%install
install -d %{buildroot}%{_sysconfdir}

install -m0644 audiolist %{buildroot}%{_sysconfdir}
install -m0644 audiolist.alsa %{buildroot}%{_sysconfdir}
install -m0644 audiolist.bestdriver %{buildroot}%{_sysconfdir}
install -m0644 niclist %{buildroot}%{_sysconfdir}
install -m0644 usblist %{buildroot}%{_sysconfdir}
install -m0644 vidlist %{buildroot}%{_sysconfdir}

