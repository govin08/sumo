#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2023 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to select mode
netedit.selectMode()

# select junctions
netedit.leftClick(referencePosition, 439, 244)
netedit.leftClick(referencePosition, 498, 174)
netedit.leftClick(referencePosition, 558, 174)
netedit.leftClick(referencePosition, 562, 274)
netedit.leftClick(referencePosition, 501, 296)
netedit.leftClick(referencePosition, 438, 299)

# join junctions
netedit.joinSelectedJunctions()

# rebuild network
netedit.rebuildNetwork()

# split and reconect
netedit.contextualMenuOperation(referencePosition, 500, 236, 14, 0, 0)

# rebuild network
netedit.rebuildNetwork()

# Check undo
netedit.undo(referencePosition, 2)

# rebuild network
netedit.rebuildNetwork()

# Check redo
netedit.redo(referencePosition, 2)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
