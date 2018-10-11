%global srcname pyrsistent
%global mod_name pyrsistent

Summary:        Persistent/Functional/Immutable data structures
Name:           python-%{srcname}
Version:        0.14.2
Release:        6%{?dist}
License:        MIT
Source0:        https://files.pythonhosted.org/packages/source/p/%{mod_name}/%{mod_name}-%{version}.tar.gz
URL:            http://github.com/tobgu/pyrsistent/

%description
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.


%package -n python%{python3_pkgversion}-%{srcname}
Summary: Persistent/Functional/Immutable data structures
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  gcc

%description -n python%{python3_pkgversion}-%{srcname}
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
#% {__python3} setup.py test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENCE.mit
%doc README.rst
%{python3_sitearch}/__pycache__/_%{srcname}_*.pyc
%{python3_sitearch}/_%{srcname}_version.py
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info/*
%{python3_sitearch}/pvectorc.cpython*.so


%changelog
* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.2-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-4
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-3
- add missing dist-tag

* Fri Apr 13 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-2
- disable tests for now

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-1
- new version 0.14.2

* Wed Sep 14 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-2
- Fix packaging errors, that would own /usr/lib64 or so.

* Tue Sep 13 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-1
- Initial packaging for PostgreSQL YUM repository, to satisfy
  pgadmin4 dependency.
