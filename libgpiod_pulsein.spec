%global gitcommit 19cff93d2bd803e49a874ec0ec7d364170908182
%global gittag master
%global gitshort %(echo %{gitcommit} | cut -c 1-7)

Name:           libgpiod_pulsein
Version:        0.git%{gitshort}
Release:        1%{?dist}
Summary:        Continuously poll line value from a GPIO chip

License:        MIT
URL:            https://github.com/adafruit/libgpiod_pulsein
Source0:        %{url}/archive/%{gittag}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:         0001-Make-variables-more-standard.patch

BuildRequires:  gcc make
BuildRequires:  libgpiod-devel
#Requires:       

%description
Continuously poll line value from a GPIO chip.
Dependency of python-adafruit-blinka.

%prep
%autosetup -n %{name}-%{gittag} -p1


%build
pushd src
%{set_build_flags}
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
popd


%install
install -m 755 -D src/libgpiod_pulsein %{buildroot}/%{_sbindir}/libgpiod_pulsein

%files
%license LICENSE
%doc README.md
%{_sbindir}/libgpiod_pulsein



%changelog
* Mon Feb 15 2021 Petr Menšík <pemensik@redhat.com>
- 
