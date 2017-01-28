Summary:	A collection manager
Name:		tellico
Version:	3.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Databases
URL:		http://tellico-project.org/
Source0:	http://www.tellico-project.org/files/%{name}-%{version}.tar.zx
Requires:	kdebase5-runtime
Requires:	kdelibs5-core
%if %{mdvver} < 201200
Requires:	kdemultimedia5
%endif
Requires:	kdepimlibs-core
BuildRequires:	libqjson0
BuildRequires:	libqjson-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdepimlibs5-devel
%if %{mdvver} < 201200
BuildRequires:	libqt5multimedia-devel
%else
BuildRequires:	libkcddb-devel
BuildRequires:	libkcompactdisc-devel
%endif
BuildRequires:	pkgconfig(libksane)
BuildRequires:	kdelibs-devel
BuildRequires:	exempi-devel
BuildRequires:	pkgconfig(libexslt0)
BuildRequires:	imagemagick
BuildRequires:	taglib-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	yaz-devel >= 3.0
BuildRequires:  qimageblitz-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	kde5-macros
BuildRequires:	qt5-devel
Obsoletes:	bookcase
Provides:	bookcase

%description
Tellico is a collection manager for KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from different web services such as amazon.com.

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/tellico.desktop
%{_kde_datadir}/mimelnk/application/x-tellico.desktop
%{_kde_datadir}/mime/packages/tellico.xml
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/apps/kconf_update/*
%{_kde_datadir}/config.kcfg/tellico_config.kcfg
%{_kde_datadir}/config/*
%{_kde_iconsdir}/hicolor/*/*/*.png

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

