/*
 * Copyright (c) 2013-2016 Cinchapi Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.cinchapi.concourse.bugrepro;

import org.junit.Assert;
import org.junit.Test;

import com.cinchapi.concourse.lang.Criteria;
import com.cinchapi.concourse.test.ConcourseIntegrationTest;
import com.cinchapi.concourse.thrift.Operator;
import com.google.common.collect.Sets;

/**
 * http://jira.cinchapi.com/browse/CON-326
 * 
 * @author Jeff Nelson
 */
public class CON326 extends ConcourseIntegrationTest {

    @Test
    public void repro() {
        client.set("sequence", 1L, 1);
        Assert.assertEquals(Sets.newHashSet(1L), client.find(Criteria.where()
                .key("sequence").operator(Operator.EQUALS).value(1).build()));
    }
}
