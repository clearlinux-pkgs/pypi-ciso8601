#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ciso8601
Version  : 2.2.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/db/50/ed16ee9a645196a29d2b7222d77e7d266f63f7a6042f2ac6cbb18a2b98e4/ciso8601-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/db/50/ed16ee9a645196a29d2b7222d77e7d266f63f7a6042f2ac6cbb18a2b98e4/ciso8601-2.2.0.tar.gz
Summary  : Fast ISO8601 date time parser for Python written in C
Group    : Development/Tools
License  : MIT
Requires: pypi-ciso8601-license = %{version}-%{release}
Requires: pypi-ciso8601-python = %{version}-%{release}
Requires: pypi-ciso8601-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ciso8601
        ========

%package license
Summary: license components for the pypi-ciso8601 package.
Group: Default

%description license
license components for the pypi-ciso8601 package.


%package python
Summary: python components for the pypi-ciso8601 package.
Group: Default
Requires: pypi-ciso8601-python3 = %{version}-%{release}

%description python
python components for the pypi-ciso8601 package.


%package python3
Summary: python3 components for the pypi-ciso8601 package.
Group: Default
Requires: python3-core
Provides: pypi(ciso8601)

%description python3
python3 components for the pypi-ciso8601 package.


%prep
%setup -q -n ciso8601-2.2.0
cd %{_builddir}/ciso8601-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641855972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ciso8601
cp %{_builddir}/ciso8601-2.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ciso8601/51613ab38cfc21e45938a266fd16b66914821c69
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ciso8601/51613ab38cfc21e45938a266fd16b66914821c69

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
