%global pypi_name asyncio-dgram
%global mod_name asyncio_dgram

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        7.rv64_nc%{?dist}
Summary:        Higher level Datagram support for Asyncio

License:        MIT
URL:            https://github.com/jsbronder/asyncio-dgram
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The goal of this package is to make implementing common patterns that
use datagrams simple and straight-forward while still supporting more
esoteric options. This is done by taking an opinionated stance on the
API that differs from parts of asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The goal of this package is to make implementing common patterns that
use datagrams simple and straight-forward while still supporting more
esoteric options. This is done by taking an opinionated stance on the
API that differs from parts of asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v test -k "not test_protocol_pause_resume" || :

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{mod_name}/
%{python3_sitelib}/%{mod_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
