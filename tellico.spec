%define iconname %{name}.png

Summary:	A book collection manager
Name:		tellico
Version:	1.3.2.1
Release:	%mkrel 1
Epoch:		1
License:	GPLv2+
Group:		Databases
URL:		http://www.periapsis.org/tellico
Source:		http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.gz
Requires:	kdebase
Requires:	kdemultimedia-kscd
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdelibs-devel 
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	imagemagick
BuildRequires:	icu-devel
BuildRequires:	libpoppler-qt-devel
BuildRequires:	chrpath
BuildRequires:	taglib-devel
BuildRequires:	kdemultimedia-devel
BuildRequires:	kdepim-devel
BuildRequires:	libcdda-devel
BuildRequires:	yaz-devel >= 3.0
BuildRequires:	tcp_wrappers-devel 
Obsoletes:	bookcase
Provides:	bookcase
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Tellico is a KDE application for keeping track of your book collection.

Features:

o Supports collections of books, bibliographic entries, videos, or music. 
o Supports any number of user-defined fields, of eight different types:
   o text, paragraph, list, checkbox, year, URL
   o tables of one or two columns.
o Handles books with multiple authors, genres, keywords, etc.
o Automatically formats titles and names
o Supports collection searching and view filtering
o Sorts and groups collection by various properties
o Automatically validates ISBN
o Allows customizable output through XSLT
o Imports Bibtex, Bibtexml, and CSV
o Exports to Bibtex, Bibtexml, CSV, and HTML
o Includes translations for more than nine languages, other than English
o Imports information directly from Amazon.com
   (US, Japan, Germany, and United Kingdom)
o Imports CDDB data
o Scans and imports audio file collections, such as mp3 or ogg
o Imports and exports to Alexandria libraries

%prep
%setup -q

%build 

%configure2_5x \
	--disable-debug \
	--disable-rpath \
	--with-xinerama \
	--enable-pch \
	--enable-new-ldflags \
	--enable-final \
	--enable-nmcheck

%make

%install
rm -rf %{buildroot}

%makeinstall_std
chrpath -d %{buildroot}%{_bindir}/*

%find_lang %{name} --with-html

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%update_mime_database

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_mime_database

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%{_bindir}/%{name}
%{_datadir}/applications/kde/tellico.desktop
%{_datadir}/mimelnk/application/x-tellico.desktop
%{_datadir}/mime/packages/tellico.xml
%{_datadir}/apps/%{name}
%{_datadir}/apps/kconf_update/*
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_datadir}/config/tellicorc
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.png
