Summary:	The convenient way of managing passwords
Summary(pl):	Wygodny sposób zarz±dzania has³ami
Name:		pwmanager
Version:	1.2.4
Release:	1
License:	GPL/LGPL
Group:		Applications
Source0:	http://dl.sourceforge.net/passwordmanager/%{name}-%{version}.tar.bz2
# Source0-md5:	e6f720af9b325bc0e7ea20c9c5e6039f
Source1:	http://dl.sourceforge.net/passwordmanager/%{name}-i18n-%{version}.tar.bz2
# Source1-md5:	b5cdd98733fdbbde6d3907345568b30e
URL:		http://passwordmanager.sourceforge.net/
BuildRequires:	bzip2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libchipcard2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PwManager is a secure password manager. With PwManager you can easily
manage your passwords. PwManager saves your passwords
blowfish-encrypted in one file, so you have to remember only one
master-password instead of all. Instead of the master-password you can
use a chipcard, so you don't have to remember a password to access the
list.

%description -l pl
PwManager jest bezpiecznym mened¿erem hase³, w którym mo¿esz ³atwo
zarz±dzaæ Twoimi has³ami. PwManager zapisuje Twoje has³a kodowane
przez blowfish w jednym pliku, wiêc musisz pamiêtaæ tylko jedno nadrzêdne
has³o zamiast wszystkich. Mo¿esz u¿yæ karty chipowej zamiast has³a
nadrzêdnego.

%prep
%setup -q -a1

%build
%configure \
	%{!?debug:--disable-rpath} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir} \
	--enable-pwmanager-smartcard \
	--enable-pwmanager-libchipcard2 \
	--enable-kwallet
%{__make}

cd %{name}-i18n-%{version}
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kdelnkdir=%{_desktopdir} \
	DESTDIR=$RPM_BUILD_ROOT

cd %{name}-i18n-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/kded/*.desktop
%{_desktopdir}/*.desktop
