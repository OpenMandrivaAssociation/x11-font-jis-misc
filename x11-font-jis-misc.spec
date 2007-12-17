Name: x11-font-jis-misc
Version: 1.0.0
Release: %mkrel 5
Summary: Xorg X11 font jis-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-jis-misc-%{version}.tar.bz2
License: CHECK
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font jis-misc

%prep
%setup -q -n font-jis-misc-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/misc

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/misc/fonts.dir
rm -f %{buildroot}%_datadir/fonts/misc/fonts.scale

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/misc/jiskan*.pcf.gz
