#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kalgebra
Version  : 20.08.2
Release  : 20
URL      : https://download.kde.org/stable/release-service/20.08.2/src/kalgebra-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/kalgebra-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/kalgebra-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kalgebra-bin = %{version}-%{release}
Requires: kalgebra-data = %{version}-%{release}
Requires: kalgebra-license = %{version}-%{release}
Requires: kalgebra-locales = %{version}-%{release}
BuildRequires : analitza-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kirigami2-dev
BuildRequires : ncurses-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsvg-dev
BuildRequires : qtwebengine-dev

%description
No detailed description available

%package bin
Summary: bin components for the kalgebra package.
Group: Binaries
Requires: kalgebra-data = %{version}-%{release}
Requires: kalgebra-license = %{version}-%{release}

%description bin
bin components for the kalgebra package.


%package data
Summary: data components for the kalgebra package.
Group: Data

%description data
data components for the kalgebra package.


%package doc
Summary: doc components for the kalgebra package.
Group: Documentation

%description doc
doc components for the kalgebra package.


%package license
Summary: license components for the kalgebra package.
Group: Default

%description license
license components for the kalgebra package.


%package locales
Summary: locales components for the kalgebra package.
Group: Default

%description locales
locales components for the kalgebra package.


%prep
%setup -q -n kalgebra-20.08.2
cd %{_builddir}/kalgebra-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602632986
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602632986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kalgebra
cp %{_builddir}/kalgebra-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/kalgebra/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kalgebra-20.08.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kalgebra/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/kalgebra-20.08.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kalgebra/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/kalgebra-20.08.2/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kalgebra/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang kalgebra
%find_lang plasma_applet_kalgebraplasmoid
%find_lang kalgebramobile

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kalgebra
/usr/bin/kalgebramobile

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kalgebra.desktop
/usr/share/applications/org.kde.kalgebramobile.desktop
/usr/share/icons/hicolor/64x64/apps/kalgebra.png
/usr/share/icons/hicolor/scalable/apps/kalgebra.svgz
/usr/share/kalgebramobile/plugins/About.qml
/usr/share/kalgebramobile/plugins/Console.qml
/usr/share/kalgebramobile/plugins/Dictionary.qml
/usr/share/kalgebramobile/plugins/Plot2D.qml
/usr/share/kalgebramobile/plugins/Plot3D.qml
/usr/share/kalgebramobile/plugins/Tables.qml
/usr/share/kalgebramobile/plugins/VariablesView.qml
/usr/share/kalgebramobile/plugins/kalgebraabout.json
/usr/share/kalgebramobile/plugins/kalgebraconsole.json
/usr/share/kalgebramobile/plugins/kalgebradictionary.json
/usr/share/kalgebramobile/plugins/kalgebraplot2d.json
/usr/share/kalgebramobile/plugins/kalgebraplot3d.json
/usr/share/kalgebramobile/plugins/kalgebratables.json
/usr/share/kalgebramobile/plugins/kalgebravariables.json
/usr/share/kalgebramobile/plugins/widgets/AddButton.qml
/usr/share/kalgebramobile/plugins/widgets/ExpressionInput.qml
/usr/share/kalgebramobile/plugins/widgets/KAlgebraMobile.qml
/usr/share/kalgebramobile/plugins/widgets/KAlgebraPage.qml
/usr/share/kalgebramobile/plugins/widgets/RealInput.qml
/usr/share/kalgebramobile/plugins/widgets/qmldir
/usr/share/katepart5/syntax/kalgebra.xml
/usr/share/kservices5/graphsplasmoid.desktop
/usr/share/metainfo/org.kde.kalgebra.appdata.xml
/usr/share/metainfo/org.kde.kalgebramobile.appdata.xml
/usr/share/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/config.ui
/usr/share/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.graphsplasmoid/metadata.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kalgebra/commands.docbook
/usr/share/doc/HTML/ca/kalgebra/index.cache.bz2
/usr/share/doc/HTML/ca/kalgebra/index.docbook
/usr/share/doc/HTML/ca/kalgebra/kalgebra-2dgraph-window.png
/usr/share/doc/HTML/ca/kalgebra/kalgebra-3dgraph-window.png
/usr/share/doc/HTML/ca/kalgebra/kalgebra-console-window.png
/usr/share/doc/HTML/ca/kalgebra/kalgebra-dictionary-window.png
/usr/share/doc/HTML/ca/kalgebra/kalgebra-main-window.png
/usr/share/doc/HTML/de/kalgebra/commands.docbook
/usr/share/doc/HTML/de/kalgebra/index.cache.bz2
/usr/share/doc/HTML/de/kalgebra/index.docbook
/usr/share/doc/HTML/de/kalgebra/kalgebra-main-window.png
/usr/share/doc/HTML/en/kalgebra/commands.docbook
/usr/share/doc/HTML/en/kalgebra/index.cache.bz2
/usr/share/doc/HTML/en/kalgebra/index.docbook
/usr/share/doc/HTML/en/kalgebra/kalgebra-2dgraph-window.png
/usr/share/doc/HTML/en/kalgebra/kalgebra-3dgraph-window.png
/usr/share/doc/HTML/en/kalgebra/kalgebra-console-window.png
/usr/share/doc/HTML/en/kalgebra/kalgebra-dictionary-window.png
/usr/share/doc/HTML/en/kalgebra/kalgebra-main-window.png
/usr/share/doc/HTML/en/kalgebra/view-fullscreen.png
/usr/share/doc/HTML/es/kalgebra/commands.docbook
/usr/share/doc/HTML/es/kalgebra/index.cache.bz2
/usr/share/doc/HTML/es/kalgebra/index.docbook
/usr/share/doc/HTML/es/kalgebra/kalgebra-main-window.png
/usr/share/doc/HTML/et/kalgebra/commands.docbook
/usr/share/doc/HTML/et/kalgebra/index.cache.bz2
/usr/share/doc/HTML/et/kalgebra/index.docbook
/usr/share/doc/HTML/it/kalgebra/commands.docbook
/usr/share/doc/HTML/it/kalgebra/index.cache.bz2
/usr/share/doc/HTML/it/kalgebra/index.docbook
/usr/share/doc/HTML/nl/kalgebra/commands.docbook
/usr/share/doc/HTML/nl/kalgebra/index.cache.bz2
/usr/share/doc/HTML/nl/kalgebra/index.docbook
/usr/share/doc/HTML/pt/kalgebra/commands.docbook
/usr/share/doc/HTML/pt/kalgebra/index.cache.bz2
/usr/share/doc/HTML/pt/kalgebra/index.docbook
/usr/share/doc/HTML/pt_BR/kalgebra/commands.docbook
/usr/share/doc/HTML/pt_BR/kalgebra/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kalgebra/index.docbook
/usr/share/doc/HTML/pt_BR/kalgebra/kalgebra-main-window.png
/usr/share/doc/HTML/sv/kalgebra/commands.docbook
/usr/share/doc/HTML/sv/kalgebra/index.cache.bz2
/usr/share/doc/HTML/sv/kalgebra/index.docbook
/usr/share/doc/HTML/uk/kalgebra/commands.docbook
/usr/share/doc/HTML/uk/kalgebra/index.cache.bz2
/usr/share/doc/HTML/uk/kalgebra/index.docbook
/usr/share/doc/HTML/uk/kalgebra/kalgebra-2dgraph-window.png
/usr/share/doc/HTML/uk/kalgebra/kalgebra-3dgraph-window.png
/usr/share/doc/HTML/uk/kalgebra/kalgebra-console-window.png
/usr/share/doc/HTML/uk/kalgebra/kalgebra-dictionary-window.png
/usr/share/doc/HTML/uk/kalgebra/kalgebra-main-window.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kalgebra/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kalgebra/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kalgebra/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kalgebra/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kalgebra.lang -f plasma_applet_kalgebraplasmoid.lang -f kalgebramobile.lang
%defattr(-,root,root,-)

